#include<iostream>
using namespace std;

int main() {
	int n, i, j, k, row, col, mincost=0, min,ed,v1,v2;
	char op;
	cout<<"Enter no. of vertices: ";
	cin>>n;
	int cost[n][n];
	int visit[n];

	for(i=0; i<n; i++)
		visit[i] = 0;

    for(i=0; i<n; i++)
        for(int j=0; j<n; j++)
            cost[i][j] = -1;


    cout<<"\nEnter the no of edges:- "<<endl;
    cin>>ed;
    
    for(i=0;i<ed;i++)
    {
        cout<<"\nEnter the v1 of edge "<<i+1;
        cin>>v1;
        cout<<"\nEnter the v2 of edge "<<i+1;
        cin>>v2;
        
        cout<<"\nEnter weight"<<endl;
        cin>>cost[v1-1][v2-1];
        cost[v2-1][v1-1]=cost[v1-1][v2-1];
        
    }
    
		visit[0] = 1;
		for(k=0; k<n-1; k++)
        {
			min = 999;
			for(i=0; i<n; i++)
			{
				for(j=0; j<n; j++)
				{
					if(visit[i] == 1 && visit[j] == 0)
					{
						if(cost[i][j] != -1 && min>cost[i][j])
						{
							min = cost[i][j];
							row = i;
							col = j;
						}
					}
				}
			}
			mincost += min;
			visit[col] = 1;
			cost[row][col] = cost[col][row] = -1;
			cout<<row+1<<"->"<<col+1<<endl;
		}
		cout<<"\nMin. Cost: "<<mincost;
	return 0;
}
