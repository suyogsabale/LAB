#include <iostream>
#include <vector>
using namespace std;

class GraphColoring {
private:
    vector<vector<int>> graph;
    vector<int> solution;
    int nv;
    int nc;

public:
    GraphColoring(const vector<vector<int>>& g, int colors,int ver) {
        graph = g;
        nv = ver;
        nc = colors;
        solution.resize(nv, -1);
    }

    bool isSafe(int vertex, int color) {    //check neighbours of vertex 
        for (int v = 0; v < nv; v++) {
            if (graph[vertex][v] == 1 && solution[v] == color) {            //v= neighbours.............if there is neighbour and it has same color then false
                return false;
            }
        }
        return true;
    }

    bool solveColor(int vertex) {
        if (vertex == nv)    //base case
        {
            return true;
        }

        for (int color = 0; color < nc; color++) {
            if (isSafe(vertex, color)) {
                solution[vertex] = color;                                                       //if safe assign vertex the color

                if (solveColor(vertex + 1)) 
                {                                                          //recursive call
                    return true;
                }
                                                                            //backtracking
                solution[vertex] = -1;
            }
        }

        return false;
    }

    vector<int> solve() {
        if (solveColor(0)) {
            return solution;
        }
        else {
            return vector<int>();
        }
    }
};

int main() {
    int nv, nc;
    cout << "Enter the number of vertices in the graph: ";
    cin >> nv;
    cout << "Enter the number of colors available: ";
    cin >> nc;

    vector<vector<int>> graph(nv, vector<int>(nv));
    cout << "Enter the adjacency matrix for the graph:\n";
    for (int i = 0; i < nv; i++) {
        for (int j = 0; j < nv; j++) {
            cin >> graph[i][j];
        }
    }

    GraphColoring gc(graph, nc,nv);   
    vector<int> solution = gc.solve();

    if (!solution.empty()) {
        cout << "Solution:\n";
        for (int i = 0; i < nv; i++) {
            cout << "Vertex " << i + 1 << " is colored with color " << solution[i] + 1 << "\n";
        }
    }
    else {
        cout << "No solution exists for the given graph and number of colors.\n";
    }

    return 0;
}
