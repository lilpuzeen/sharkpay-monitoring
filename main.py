import time

from build_xml import build_xml
from config import config
from loguru import logger


def main():
    xml = build_xml(config['pairs'])
    with open('rates.xml', 'w', newline='\r\n') as f:
        f.write(xml)
    logger.info(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] rates.xml updated")

if __name__ == '__main__':
    main()
