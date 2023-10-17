import sys
import time


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    start_time = time.time()

    for i, item in enumerate(lst):
        percentage = (i + 1) / total
        bar_length = 60
        arrow = '=' * int(round(percentage * bar_length) - 1) + '>'
        spaces = ' ' * (bar_length - len(arrow))

        elapsed_time = time.time() - start_time
        rate = (i + 1) / elapsed_time
        rate_info = f"{rate:.2f}it/s"

        # Display
        sys.stdout.write(f"\r[{arrow + spaces}] {i + 1}/{total} {rate_info}")
        sys.stdout.flush()

        yield item

    sys.stdout.write("\n")
    sys.stdout.flush()
