#include <bits/stdc++.h>
#include <iostream>
#include <conio.h>
using namespace std;
void Edge(vector<int> adj[], int u, int v)
{
	adj[u].push_back(v);
	adj[v].push_back(u);
}


void displaygraph(vector<int> adj[], int V)
{
	for (int v = 0; v < V; ++v) {
		cout << "\n Adjacency list of vertex " << v
			<< "\n head ";
		for ( auto x : adj[v])
			cout << "-> " << x;
		cout<<"\n";
	}
}


int main()
{
	int V = 5;
	vector<int> adj[V];
	Edge(adj, 0, 1);
	Edge(adj, 0, 4);
	Edge(adj, 1, 2);
	Edge(adj, 1, 3);
	Edge(adj, 1, 4);
	Edge(adj, 2, 3);
	Edge(adj, 3, 4);
	displaygraph(adj, V);
	return 0;
}
