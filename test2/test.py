import logging
import argparse

# Make output directory
import os
if not os.path.exists('/output'):
    os.makedirs('/output')

# get a file logger
def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('/output/test.log')
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    return logger

def add(x, y):
    return x + y

if __name__ == '__main__':
    logger = get_logger()
    logger.info('test')
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=int, required=True)
    parser.add_argument('--y', type=int, required=True)
    args = parser.parse_args()

    print(add((args.x), args.y))
    logger.info('x: {}, y: {}'.format(args.x, args.y))

    result = add(args.x, args.y)
    logger.info('result: {}'.format(result))

    # Save the result to a file in /output
    with open('/output/result.txt', 'w') as f:
        f.write(str(result))

