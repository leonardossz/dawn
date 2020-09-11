from __future__ import unicode_literals

import sys
import boto3

from prompt_toolkit import PromptSession
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers.sql import SqlLexer

rdsData = boto3.client('rds-data')


def execute(cluster_arn, secret_arn, db, sql_str) -> str:
    return rdsData.execute_statement(
        resourceArn=cluster_arn,
        secretArn=secret_arn,
        database=db,
        sql=sql_str)


def main(*args):
    cluster_arn, secret_arn, db = args

    session = PromptSession(lexer=PygmentsLexer(SqlLexer))

    while True:
        try:
            sql_str = session.prompt(f'{db} | mysql> ')
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
        else:
            if sql_str:
                res = execute(cluster_arn, secret_arn, db, sql_str)
                print(res)


if __name__ == '__main__':
    main(*sys.argv[1:])
