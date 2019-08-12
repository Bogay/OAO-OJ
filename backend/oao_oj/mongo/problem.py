import pymongo
import os

from oao_oj.config import PROB_COL, PROB_DIR
from json import loads as json_loads
from flask import jsonify
from shutil import rmtree

CLIENT = pymongo.MongoClient('mongodb://localhost:27017/')
DB = CLIENT['OAO-OJ']
COLL = DB[PROB_COL]


class Problem():
    '''An api for accessing problems in MongoDB.'''
    def __init__(self, pid: str):
        self.pid = pid


    @classmethod
    def add(cls, pid: str, data: dict):
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
            None if the pid exists, Problem(pid) otherwise.

        '''
        prob = cls(pid)

        if prob.json:
            return None

        # Insert the problem to DB
        title = data.get('title', '')
        COLL.insert_one({
            'pid': pid,
            'title': title
        })

        ppath = f'{PROB_DIR}/{pid}'
        os.makedirs(ppath, exist_ok=True)

        # Write the problem description
        desc = data.get('desc', '')
        with open(f'{ppath}/prob.md', 'w') as f:
            f.write(desc)

        # Write the info.json
        info = data.get('info', '')
        with open(f'{ppath}/info.json', 'w') as f:
            f.write(info)

        os.makedirs(f'{ppath}/testdatas', exist_ok=True)

        # Write the testdatas
        tds = json_loads(data.get('testdatas', '{}'))
        for td in tds:
            for i, ex in enumerate(['in', 'out']):
                with open(f'{ppath}/testdatas/{td}.{ex}', 'w') as f:
                    f.write(tds[td][i])

        return prob


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
    def json(self):
        '''JSON with detail of the problem.
        None if the problem not exists, a string otherwise.
        '''
        prob = COLL.find_one({'pid': self.pid})

        if not prob:
            return None

        json = jsonify({
            'pid': prob['pid'],
            'title': prob['title'],
            'desc': self.desc
        })

        return json


    def update(self, data):
        '''A method for updating the problem'''
        return 'El psy congroo'


    def delete(self):
        '''A method for deleting the problem'''
        count = COLL.delete_one({'pid': self.pid}).deleted_count

        if count:
            rmtree(f'{PROB_DIR}/{self.pid}', ignore_errors=True)

        return count


def get_all_problems():
    ''' A function for get all problems in MongoDB.

    Returns:
        A list of pid and title for each problem.

    '''
    ps = [*COLL.find({}, {'_id': 0, 'pid': 1, 'title': 1})]
    json = jsonify([{
        'Id': p['pid'], 
        'Name': p['title'], 
        'Status':0,
        'Submissions AC%': 0,
        'Users AC%': 0
    } for p in ps])

    return json
