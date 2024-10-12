import timeit

from compare.kmp_search import kmp_search
from compare.boyer_moore_search import boyer_moore_search
from compare.rabin_karp_search import rabin_karp_search


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def measure_algorithm(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=1)


def compare_algorithms(text_file, algorithms, patterns):
    text1 = read_file(text_file)

    results = {}

    print(f"\nResults for file: {text_file}")
    results[text_file] = {}
    for algorithm_name, algorithm_func in algorithms.items():
        results[text_file][algorithm_name] = {}
        for pattern_name, pattern in patterns.items():
            execution_time = measure_algorithm(algorithm_func, text1, pattern)
            print(
                f"Algorithm {algorithm_name}, substring '{pattern_name}': {execution_time:.6f} sec"
            )
            results[text_file][algorithm_name][pattern_name] = execution_time

    return results


if __name__ == "__main__":
    text_file1 = "compare/article1.txt"
    patterns1 = {
        "Existing substring": "Ознаки того, що задачу можливо вирішити за допомогою жадібного алгоритму:",
        "Nonexistent substring": "Зменшення розміру блоку дозволяє зменшити втрати пам’яті",
    }

    text_file2 = "compare/article2.txt"
    patterns2 = {
        "Existing substring": "Зменшення розміру блоку дозволяє зменшити втрати пам’яті",
        "Nonexistent substring": "Ознаки того, що задачу можливо вирішити за допомогою жадібного алгоритму:",
    }

    algorithms = {
        "Boyer-Moore": boyer_moore_search,
        "Knuth-Morris-Pratt": kmp_search,
        "Rabin-Karp": rabin_karp_search,
    }

    compare_algorithms(text_file1, algorithms, patterns1)
    compare_algorithms(text_file2, algorithms, patterns2)
