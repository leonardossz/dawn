from __future__ import unicode_literals

__copyright__ = 'Copyright 2020 See AUTHORS'
__license__ = 'See LICENSE'

import json
import sys
import boto3

from prompt_toolkit import PromptSession
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers.sql import SqlLexer
from pygments.lexers.data import JsonLexer
from pygments import highlight
from pygments.formatters.terminal import TerminalFormatter

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
    json_lexer = JsonLexer()
    term_formatter = TerminalFormatter()

    while True:
        try:
            print('Use CTRL-d to exit.')
            sql_str = session.prompt(f'{db} | mysql> ')
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
        else:
            if sql_str:
                res = execute(cluster_arn, secret_arn, db, sql_str)
                json_str = json.dumps(res, indent=4, sort_keys=True)
                print(highlight(json_str, json_lexer, term_formatter))


if __name__ == '__main__':
    main(*sys.argv[1:])
