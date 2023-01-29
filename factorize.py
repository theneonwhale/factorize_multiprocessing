import time
import logging


def factorize(*number):
    start = time.time()
    logging.debug(f'Start time: {round(start, 10)}')
    results = []
    for item in number:
        logging.debug('-----------------')
        logging.debug(f'Item: {item}')
        start_item = time.time()
        logging.debug(f'Start item time: {round(start_item, 10)}')
        result = [i for i in range(1, item + 1) if item % i == 0]
        # logging.debug(f'Result: {result}')
        end_item = time.time()
        logging.debug(f'End item time: {round(end_item, 10)}')
        work_item_time = end_item - start_item
        logging.debug(f'Execution item time: {round(work_item_time, 10) }')
        logging.debug('-----------------')
        results.append(result)
    logging.debug(f'Results: {results}')
    end = time.time()
    work_time = end - start
    logging.debug(f'Execution time: {round(work_time, 10)}')
    return results
    # raise NotImplementedError() # Remove after implementation


def main():
    logging.basicConfig(level=logging.DEBUG, format="%(funcName)s %(message)s")

    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]


if __name__ == '__main__':
    main()
