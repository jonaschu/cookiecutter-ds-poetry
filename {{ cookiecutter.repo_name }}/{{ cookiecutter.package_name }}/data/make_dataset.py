# -*- coding: utf-8 -*-
from dotenv import find_dotenv, load_dotenv
from pathlib import Path
import logging

def main():
    """ 
    """
    logger = logging.getLogger(__name__)
    logger.info('main function was called')



if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
