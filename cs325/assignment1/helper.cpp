#include "helper.h"
#include <algorithm>
#include <iostream>
#include <fstream>
#include <chrono>
#include <random>
#include <sstream>

std::vector<std::vector<int>> read_numbers(std::string fname) {
  std::fstream fs(fname);

  if(!fs) {
    std::cout << "Failed to open file." << std::endl;
  }

  std::vector<std::vector<int>> lines;

  std::string line;
  while(std::getline(fs, line, '\n')) {
    std::stringstream linestream(line);

    std::vector<int> nums;
    std::string num;
    while(std::getline(linestream, num, ',')) {
      nums.push_back(std::stoi(num));
    }

    lines.push_back(nums);
  }

  return lines;
}

std::vector<int> random_numbers(int length) {
  std::vector<int> numbers;

  for(int i = 0; i < length; i++) {
    numbers.push_back(i);
  }

  unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
  std::shuffle(numbers.begin(), numbers.end(), std::default_random_engine(seed));

  return numbers;
}
