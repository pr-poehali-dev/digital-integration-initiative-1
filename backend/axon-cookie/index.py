import os
import re

def handler(event: dict, context) -> dict:
    """
    Читает куку _axwrt из запроса и устанавливает первичную куку axwrt
    для улучшенной идентификации пользователей Axon Pixel.
    """
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, X-Cookie',
                'Access-Control-Max-Age': '86400',
            },
            'body': ''
        }

    cookie_header = event.get('headers', {}).get('X-Cookie', '') or ''

    axwrt_value = None
    for part in cookie_header.split(';'):
        part = part.strip()
        if part.startswith('_axwrt='):
            axwrt_value = part[len('_axwrt='):]
            break

    if not axwrt_value or not re.match(r'^[a-f0-9\-]{36}$', axwrt_value):
        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': 'ok'
        }

    from datetime import datetime, timedelta
    expires = (datetime.utcnow() + timedelta(days=365)).strftime('%a, %d %b %Y %H:%M:%S GMT')

    host = event.get('headers', {}).get('host', '') or event.get('headers', {}).get('Host', '')
    domain = host.split(':')[0]
    if domain.startswith('www.'):
        domain = domain[4:]
    if '.' in domain:
        domain = '.' + domain

    cookie_value = f"axwrt={axwrt_value}; Expires={expires}; Domain={domain}; Path=/; SameSite=Lax"

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'X-Set-Cookie': cookie_value,
        },
        'body': 'ok'
    }
