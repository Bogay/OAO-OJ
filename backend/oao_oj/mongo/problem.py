import os

from oao_oj.config import OJ_DB, PROB_COL, PROB_DIR, TEST_DIR
from oao_oj.error import BadRequest, NotFound, NotAcceptable

from json import dumps as json_dumps, loads as json_loads
from flask import jsonify
from shutil import rmtree

COLL = OJ_DB[PROB_COL]


class Problem():
    '''An api for accessing problems in MongoDB.'''
    def __init__(self, pid: str):
        self.pid = pid


    @classmethod
    def add(cls, pid: str, data):
        '''A class method for adding the new problem to DB.

        Args:
            pid: The id of the problem to be added.
            data: More information about the problem,
                  it would be something like:
                {
                   'title': 'ABC',
                   'desc' : '# MarkDown',
                   'info' : '{ "testdatas": [ ["01", 3, 512], ["02", 3, 512] ] }',
                   'testdatas': '{"01": ["01.in", "01.out"], "02": ["02.in", "02.out"]}'
                }

        Returns:
            Problem instance: Problem(pid).

        '''

        # Check data
        if data == None:
            raise NotAcceptable('Invalid Content-Type or JSON data')

        # Check pid
        if COLL.find_one({'pid': pid}):
            raise BadRequest('Problem exists.')

        # Get title
        title = data.get('title', '')

        # Check status
        status = data.get('status', 1)
        if status not in range(3):
            raise BadRequest('Invalid status.')

        # Insert the problem to DB
        COLL.insert_one({
            'pid': pid,
            'title': title,
            'status': status
        })

        # Make dir for new problem
        ppath = f'{PROB_DIR}/{pid}'
        os.makedirs(ppath, exist_ok=True)

        # Write the problem description
        desc = data.get('desc', '')
        with open(f'{ppath}/prob.md', 'w') as f:
            f.write(desc)

        # Write the info.json
        info = json_dumps(data.get('info', {}))
        with open(f'{ppath}/info.json', 'w') as f:
            f.write(info)

        # Make dir for testdatas
        os.makedirs(f'{ppath}/testdatas', exist_ok=True)

        # Write the testdatas
        tds = data.get('testdatas', {})
        for td in tds:
            for i, ex in enumerate(['in', 'out']):
                with open(f'{ppath}/testdatas/{td}.{ex}', 'w') as f:
                    f.write(tds[td][i])

        return cls(pid)


    @property
    def desc(self) -> str:
        '''Description of the problem.
        '''
        try:
            with open(f'{PROB_DIR}/{self.pid}/prob.md') as f:
                desc = f.read()
        except:
            desc = 'Error when reading problem\'s description!'

        return desc


    @property
    def info(self):
        try:
            with open(f'{PROB_DIR}/{self.pid}/info.json') as f:
                info = json_loads(f.read())
        except:
            info = {'testdatas': [['Error']]}

        return info


    @property
    def testdatas(self):
        testdatas = {}
        tds = self.info.get('testdatas', [])
        for td in tds:
            datas = []
            for ex in ['in', 'out']:
                try:
                    with open(f'{PROB_DIR}/{self.pid}/{TEST_DIR}/{td[0]}.{ex}') as f:
                        datas.append(f.read())
                except:
                    datas.append(f'Error when reading {td[0]}.{ex}!')
            testdatas[td[0]] = datas

        return testdatas


    def detail(self):
        '''A dict with detail of the problem.
        None if the problem not exists, a dict otherwise.
        '''
        prob = COLL.find_one({'pid': self.pid}, {'_id': False})

        if not prob:
            raise NotFound('Problem not exists.')

        return prob


    def update(self, data):
        '''A method for updating the problem'''

        # Check data
        if not data or None != data.get('status') not in range(3):
            raise NotAcceptable('Invalid Content-Type or JSON data')

        # Get update data
        update_data = {k: data[k] for k in ['title', 'status'] if data.get(k) != None}
        if not update_data:
            raise NotFound('Nothing to update.')

        # Update problem
        result = COLL.update_one({'pid': self.pid}, {'$set': update_data})
        if not result.matched_count:
            raise NotFound('Problem not exists.')

        ppath = f'{PROB_DIR}/{self.pid}'

        # Update problem description
        desc = data.get('desc')
        if desc != None:
            with open(f'{ppath}/prob.md', 'w') as f:
                f.write(desc)

        # Update info.json
        info = data.get('info')
        if info != None:
            with open(f'{ppath}/info.json', 'w') as f:
                f.write(json_dumps(info))

        # Update testdatas
        tds = data.get('testdatas', {})
        for td in tds:
            for i, ex in enumerate(['in', 'out']):
                with open(f'{ppath}/testdatas/{td}.{ex}', 'w') as f:
                    f.write(tds[td][i])


    def delete(self):
        '''A method for deleting the problem'''
        count = COLL.delete_one({'pid': self.pid}).deleted_count
        if not count:
            raise NotFound('Problem not exists.')

        rmtree(f'{PROB_DIR}/{self.pid}', ignore_errors=True)


def get_all_problems():
    ''' A function for get all problems in MongoDB.

    Returns:
        A list of pid and title for each problem.

    '''
    ps = [*COLL.find({}, {'_id': False})]

    return ps
