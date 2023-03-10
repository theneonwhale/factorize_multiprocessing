import time
import logging


logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def factorize(*number):
    start = time.time()
    results = []
    for item in number:
        result = [i for i in range(1, item + 1) if item % i == 0]
        results.append(result)
    logger.debug(f'Results: {results}')
    end = time.time()
    work_time = end - start
    logger.debug(f'Execution time: {round(work_time, 10)}')
    return results


def main():
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    logger.debug(f'Everything is ok!')


if __name__ == '__main__':
    main()
