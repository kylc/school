#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>
#include <ctime>

#include "helper.h"

int brute_force(std::vector<int> numbers) {
  int inversions = 0;
  for(size_t i = 0; i < numbers.size(); i++) {
    for(size_t j = i + 1; j < numbers.size(); j++) {
      if(numbers[i] > numbers[j]) {
        inversions++;
      }
    }
  }

  return inversions;
}

int naive_divide_and_conquer(std::vector<int> numbers) {
  if(numbers.size() % 2 != 0) {
    numbers.insert(numbers.begin(), 0);
  }

  if(numbers.size() == 2) {
    return numbers[0] > numbers[1] ? 1 : 0;
  }

  int split = floor(numbers.size() / 2);

  std::vector<int> l(numbers.begin(), numbers.begin() + split);
  std::vector<int> r(numbers.begin() + split, numbers.end());

  int inversions = 0;
  for(size_t i = 0; i < l.size(); i++) {
    for(size_t j = 0; j < r.size(); j++) {
      if(l[i] > r[j]) {
        inversions++;
      }
    }
  }

  return inversions + naive_divide_and_conquer(l) + naive_divide_and_conquer(r);
}

int merge_and_count(std::vector<int> numbers) {
  if(numbers.size() % 2 != 0) {
    numbers.insert(numbers.begin(), 0);
  }

  if(numbers.size() == 2) {
    return numbers[0] > numbers[1] ? 1 : 0;
  }

  int split = floor(numbers.size() / 2);

  std::vector<int> l(numbers.begin(), numbers.begin() + split);
  std::vector<int> r(numbers.begin() + split, numbers.end());

  std::vector<int> lsorted(l);
  std::vector<int> rsorted(r);

  std::sort(lsorted.begin(), lsorted.end());
  std::sort(rsorted.begin(), rsorted.end());

  int inversions = 0;
  for(size_t ri = 0; ri < rsorted.size(); ri++) {
    for(size_t li = 0; li < lsorted.size(); li++) {
      if(lsorted[li] > rsorted[ri]) {
        inversions += l.size() - li;
        break;
      }
    }
  }

  return inversions + merge_and_count(l) + merge_and_count(r);
}

int main(int argc, char **argv) {
  /*
  std::vector<std::vector<int>> lines = read_numbers("test_in.txt");

  for(size_t i = 0; i < lines.size(); i++) {
    std::vector<int> all_numbers = lines[i];

    int result = merge_and_count(all_numbers);
    
    std::cout << result << std::endl;
  }
  */

  std::vector<int> lengths = { 1000, 2000, 3000, 4000, 5000, 10000, 20000,
    30000, 40000, 50000 };

  for(size_t i = 0; i < lengths.size(); i++) {
    clock_t start = clock();

    for(size_t j = 0; j < 10; j++) {
      std::vector<int> nums = random_numbers(lengths[i]);

      merge_and_count(nums);
    }

    clock_t end = clock();

    double time_per_run = (double (end - start)) / CLOCKS_PER_SEC / 10;
    std::cout << lengths[i] << "," << time_per_run << std::endl;
  }
}
