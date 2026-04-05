"""Array algorithms package."""

from algonest.arrays.dutch_flag import partition_by_pivot, sort_three_values
from algonest.arrays.intervals import insert_interval, merge_intervals, non_overlapping_count
from algonest.arrays.kadane import max_subarray_sum
from algonest.arrays.matrix import diagonal_traversal, set_zeroes, transpose
from algonest.arrays.next_permutation import next_permutation, prev_permutation
from algonest.arrays.prefix_sum import prefix_sum, range_sum, subarray_sum_equals_k
from algonest.arrays.reverse import reverse_array, reverse_subarray, reverse_words
from algonest.arrays.rotate import rotate_left, rotate_matrix_90, rotate_right, spiral_order
from algonest.arrays.sliding_window import longest_unique_substring, max_sum_subarray_k
from algonest.arrays.two_pointers import container_with_water, remove_duplicates, two_sum_sorted

__all__ = [
	"max_sum_subarray_k",
	"longest_unique_substring",
	"two_sum_sorted",
	"remove_duplicates",
	"container_with_water",
	"prefix_sum",
	"range_sum",
	"subarray_sum_equals_k",
	"max_subarray_sum",
	"sort_three_values",
	"partition_by_pivot",
	"rotate_left",
	"rotate_right",
	"rotate_matrix_90",
	"spiral_order",
	"next_permutation",
	"prev_permutation",
	"merge_intervals",
	"insert_interval",
	"non_overlapping_count",
	"transpose",
	"set_zeroes",
	"diagonal_traversal",
	"reverse_array",
	"reverse_subarray",
	"reverse_words",
]
