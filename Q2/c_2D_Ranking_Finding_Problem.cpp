// source : https://hackmd.io/@Inversionpeter/Skh3CqK1O

#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int ranks[10000];

struct point {
	int x, y, index;

	bool operator<(const point &other) const {
		if (this->x != other.x)
			return this->x < other.x;
		return this->y > other.y;
	}
} points[10000], buffer[10000];

void Rank2D(int lower, int upper) {
	if (upper - lower <= 1)
		return;
	int middle = (lower + upper) >> 1, medianX = points[middle].x, counts = 0, i = lower, j = middle, k = lower;
	Rank2D(lower, middle); Rank2D(middle, upper);
	while (i < middle || j < upper) {
		if (i == middle) {
			buffer[k] = points[j]; ranks[buffer[k].index] += counts;
			++j; ++k;
		}
		else if (j == upper) {
			buffer[k] = points[i];
			++i; ++k;
		}
		else if (points[i].y < points[j].y) {
			buffer[k] = points[i]; ++counts;
			++i; ++k;
		}
		else {
			buffer[k] = points[j]; ranks[buffer[k].index] += counts;
			++j; ++k;
		}
	}
	for (i = lower; i < upper; ++i)
		points[i] = buffer[i];
}

int main() {
	cin.sync_with_stdio(false); cin.tie(nullptr);
	int amount;
	// while (cin >> amount) {
	// 	memset(ranks, 0, sizeof(ranks));
	// 	for (int i = 0; i < amount; ++i) {
	// 		cin >> points[i].x >> points[i].y;
	// 		points[i].index = i;
	// 	}
	// 	sort(points, points + amount);
	// 	Rank2D(0, amount);
	// 	for (int i = 0; i < amount; ++i)
	// 		cout << ranks[i] << '\n';
	// }
	point p1 ;
	point p2 ;
	p1.x=1;
	p1.y=1;
	p2.x=1;
	p2.y=2;
	if(p1 < p2){
		printf("yyyyyyyyy\n");
	}else{
		printf("nnnnnnnnn\n");
	}

	
}