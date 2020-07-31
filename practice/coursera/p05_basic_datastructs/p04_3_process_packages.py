# python3

from collections import deque, namedtuple
from pathlib import Path
from sys import stdin

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()

    def process(self, request):
        q = self.finish_time
        a = request.arrived_at
        t = request.time_to_process
        s = a # starting time
        while len(q) > 0 and q[0] <= a:
            s = max(a, q.popleft())
        if len(q) > 0 and len(q) < self.size:
            s = max(a, q[-1])
        elif len(q) == self.size:
            return Response(True, t)
        q.append(s + t)
        return Response(False, s)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def get_inputs(f):
    buf_siz, n_reqs = map(int, next(f).split())
    reqs = []
    for _ in range(n_reqs):
        reqs.append(Request(*map(int, next(f).split())))
    buf = Buffer(buf_siz)
    return reqs, buf


def run_tests():
    testdir = Path('tests3')
    all_passed = True
    results = {}
    for n in range(1, 23):
        input_file = testdir / f'{n:02d}'
        with open(input_file) as f:
            reqs, buf = get_inputs(f)
        resps = process_requests(reqs, buf)
        ans = [(resp.started_at if not resp.was_dropped else -1)
               for resp in resps]
        output_file = testdir / f'{n:02d}.a'
        with open(output_file) as f:
            out = list(map(int, f.read().split()))
        if ans != out:
            all_passed = False
            print(f'Failed at test#{n}')
            results[n] = (ans, out)
    if all_passed:
        print('Passed all tests')
    return results


def main():
    requests, buffer = get_inputs(stdin)
    responses = process_requests(requests, buffer)
    # print(responses)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()

