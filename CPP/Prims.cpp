#include<iostream>
using namespace std;

int main() {
	int n, i, j, k, row, col, mincost=0, min,ed,v1,v2;
	cout<<"Enter no. of vertices: ";
	cin>>n;
	int cost[n][n];   //n*n matrix to store all costs
	int visit[n];		// array to marks node visits

	for(i=0; i<n; i++)
		visit[i] = 0;		//init to 0

    for(i=0; i<n; i++)
        for(int j=0; j<n; j++)
            cost[i][j] = -1;		//init to -1


    cout<<"\nEnter the no of edges:- "<<endl;
    cin>>ed;
    
    for(i=0;i<ed;i++)
    {
        cout<<"\nEnter the v1 of edge "<<i+1;			//read vertices in human count
        cin>>v1;
        cout<<"\nEnter the v2 of edge "<<i+1;
        cin>>v2;
        
        cout<<"\nEnter weight"<<endl;
        cin>>cost[v1-1][v2-1];							//insert the weight for both the vertices in dec count
        cost[v2-1][v1-1]=cost[v1-1][v2-1];
        
    }
    
		visit[0] = 1;				//mark 0th index visited
		for(k=0; k<n-1; k++)
        {
			min = 999;        //set min to largest val
			for(i=0; i<n; i++)
			{
				for(j=0; j<n; j++)
				{
					if(visit[i] == 1 && visit[j] == 0)					//if i is visited but j is not
					{
						if(cost[i][j] != -1 && min>cost[i][j])			//if cost of edge exist && is less than min 	
						{
							min = cost[i][j];										//then update min & assign i,j to row col
							row = i;
							col = j;
						}
					}
				}
			}
			mincost += min;												//accumalte min to find minimal cost		
			visit[col] = 1;												//mark col/j visited
			cost[row][col] = cost[col][row] = -1;						//delete the edge weight from both vertices
			cout<<row+1<<"->"<<col+1<<endl;								//print in vertices in human count
		}
		cout<<"\nMin. Cost: "<<mincost;
	return 0;
}
