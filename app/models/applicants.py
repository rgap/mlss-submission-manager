# Author: Alex Ksikes

# TODO:
# - search should be improved, currently does not allow to search across all fields.

import web
from config import db

def get_where(context='', query=None, user_id=None):
    where = 'status is NULL or status is not NULL'
    
    # if a context is entered
    if context == 'new':
        where = 'status is NULL'
    elif context == 'pending':
        where = 'referee_rating is NULL'
    elif context == 'admitted':
        where = 'status = "admitted" and grant_amount = 0'
    elif context == 'rejected':
        where = 'status = "rejected"'
    elif context == 'attendee':
        where = 'status = "attendee"'
    elif context == 'scholarship_recipient':
        where = 'status = "admitted" and grant_amount > 0'
    elif user_id and context == 'reviewed':
        user_id = web.sqlquote(str(user_id))
        where = 'a.id = v.applicant_id and v.user_id = %s' % user_id 
#        (a.id = c.applicant_id and c.user_id = %s)''' % (user_id, user_id)
    
    # if in search mode
    if query:
        columns = 'first_name, last_name, a.email, affiliation, department, referee_name, status, \
        occupation, website, interests'.split(', ')
        query = web.sqlquote('%%' + query.encode('utf-8') + '%%')
        
        where = (' like %s or ' % query).join(columns)
        where += ' like %s' % query
        where += ' or concat(first_name, " ", last_name) like ' + query
    
    return where
    
def query(context='', query=None, offset=0, limit=50, order='creation_ts desc', user_id=None):
    where = get_where(context, query, user_id)

    what = '''
    a.id, a.first_name, a.last_name, a.email, a.website, a.affiliation, a.affiliated, a.department, a.interests, a.degree, a.occupation, a.secret_md5, a.referee_name, a.referee_email, a.referee_affiliation, a.referee_rating, a.creation_ts, a.update_ts, a.status, a.decided_by_user_id, a.calculated_vote, a.nationality, a.country, a.pascal_member, a.travel_support, a.travel_support_budget, a.gender, a.grant_amount, 
    (select group_concat(u.nickname separator ', ') from votes as v, users as u 
     where v.user_id = u.id and v.applicant_id = a.id) as voters,
    (select count(*) from votes as v, users as u 
     where v.user_id = u.id and v.applicant_id = a.id) as number_votes,
    (select group_concat(distinct u.nickname separator ', ') from comments as c, users as u 
     where c.user_id = u.id and c.applicant_id = a.id) as commenters,
    (select count(*) from comments as c, users as u 
     where c.user_id = u.id and c.applicant_id = a.id) as number_comments,
    (select nickname from users as u 
     where u.id = a.decided_by_user_id) as decided_by_nickname'''
    
    table = 'applicants as a'
    if user_id and context == 'reviewed':
        table = 'applicants as a, votes as v, comments as c'
    
    results = db.select(table, 
        what = what,
        where = where,
        offset = offset,
        limit = limit,
        order = order)

    count = int(db.select(table, what='count(distinct a.id) as c', where=where)[0].c)
    
    return (results, count)

def get_by_id(id):
    return web.listget(
        db.select('applicants as a, users as u', 
            vars=dict(id=id), 
            what = 'a.*, nickname',
            where='a.id=$id and (u.id = a.decided_by_user_id or a.decided_by_user_id is NULL)'), 0, {})

def admit(ids, user_id):
    ids = web.sqllist(map(str, ids))
    db.update('applicants', 
        where = 'id in (%s)' % ids,
        status = 'admitted', decided_by_user_id=user_id)
    
def reject(ids, user_id):
    ids = web.sqllist(map(str, ids))
    db.update('applicants', 
        where = 'id in (%s)' % ids,
        status = 'rejected', decided_by_user_id=user_id)

def undecide(ids, user_id):
    ids = web.sqllist(map(str, ids))
    db.update('applicants', 
        where = 'id in (%s)' % ids,
        status = None, decided_by_user_id=user_id)

def make_attendee(ids, user_id):
    print(ids)
    ids = web.sqllist(map(str, ids))
    db.update('applicants', 
        where = 'id in (%s)' % ids,
        status = 'attendee', decided_by_user_id=user_id)

def grant(user_id, id, amount):
    db.update('applicants', 
        where = 'id = %s' % id,
        grant_amount = amount, granted_by_user_id=user_id)

def add_comment(id, comment):
    db.update('applicants', 
        vars = dict(id=id),
        where = 'id = $id',
        comment = comment)

def rate(ids, score):
    ids = web.sqllist(map(str, ids))
    db.update('applicants', 
        where = 'id in (%s)' % ids,
        score = score)

def get_counts():
    counts = web.storage(new=0, pending=0, all=0, admitted=0, rejected=0, reviewed=0, scholarship_recipient=0, attendee=0)
    for context in counts.keys(): 
        counts[context] = db.select('applicants', 
            what = 'count(*) as c', 
            where = get_where(context))[0].c
    return counts

def get_by_secret_md5(secret_md5):
    return web.listget(db.select(
        'applicants', 
        vars = dict(md5=secret_md5),
        where = 'secret_md5 = $md5'), 0, False)
    
def get_dummy_record():
    return web.storage(first_name='Applicant', last_name='Name', email='', referee_name='Referee Name')

def get_stats():
    stats = web.storage(total=0, undecided=0, admitted=0, rejected=0, attendee=0, scholarships=0, allocated_amount=0)
    
    results = db.select('applicants', 
        what = 'status, count(id) as c',
        group = 'status')
    
    for r in results:
        if r.status is None: r.status = 'undecided'
        stats[r.status] = r.c
    
    stats.allocated_amount = db.select('applicants', 
        what = 'sum(grant_amount) as amount')[0].amount
    stats.total = int(db.select('applicants', what='count(distinct id) as c')[0].c)
    stats.scholarships = int(db.select('applicants', what='count(distinct id) as c', where=get_where('scholarship_recipient'))[0].c)
    stats.admitted = int(db.select('applicants', what='count(distinct id) as c', where=get_where('admitted'))[0].c)

    return stats

def update_applicant(id, document_id, first_name, last_name):
    db.update('applicants',
              where = 'id = %s' % id,
              document_id = document_id,
              first_name = first_name,
              last_name = last_name
              )

def update_applicant_user(email, username, password):
    db.update('applicants',
              where = "email = '%s'" % email,
              username = username,
              password = password
              )

def get_applicants(context='', query=None, order='creation_ts asc'):
    where = get_where(context, query)

    what = '''
    a.id, a.first_name, a.last_name, a.email, a.website, a.affiliation, a.affiliated, a.department, a.interests, a.degree, a.occupation, a.secret_md5, a.referee_name, a.referee_email, a.referee_affiliation, a.referee_rating, a.creation_ts, a.update_ts, a.status, a.decided_by_user_id, a.calculated_vote, a.nationality, a.country, a.pascal_member, a.travel_support, a.travel_support_budget, a.gender, a.grant_amount, 
    (select group_concat(u.nickname separator ', ') from votes as v, users as u 
     where v.user_id = u.id and v.applicant_id = a.id) as voters,
    (select count(*) from votes as v, users as u 
     where v.user_id = u.id and v.applicant_id = a.id) as number_votes,
    (select group_concat(distinct u.nickname separator ', ') from comments as c, users as u 
     where c.user_id = u.id and c.applicant_id = a.id) as commenters,
    (select count(*) from comments as c, users as u 
     where c.user_id = u.id and c.applicant_id = a.id) as number_comments,
    (select nickname from users as u 
     where u.id = a.decided_by_user_id) as decided_by_nickname'''

    table = 'applicants as a'

    results = db.select(table,
        what = what,
        where = where,
        order = order)

    count = int(db.select(table, what='count(distinct a.id) as c', where=where)[0].c)

    return (results, count)
