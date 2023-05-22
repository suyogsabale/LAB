#include<iostream>
#include<vector>
#include<queue>
#include<stack>
using namespace std;
//add the edge in graph
void edge(vector<int>adj[],int u,int v){
  adj[u].push_back(v);
}
//function for bfs traversal
void bfs(int s,vector<int>adj[],bool visit[]){
  queue<int>q;//queue in STL
  q.push(s);
  visit[s]=true;
  while(!q.empty()){
    int u=q.front();
    cout<<u<<" ";
    q.pop();
//loop for traverse
    for(int i=0;i<adj[u].size();i++){
      if(!visit[adj[u][i]]){
        q.push(adj[u][i]);
        visit[adj[u][i]]=true;
      }
    }
  }
}
//function for dfs traversal
void dfs(int s,vector<int>adj[],bool visit[]){
  stack<int>stk;//stack in STL
  stk.push(s);
  visit[s]=true;
  while(!stk.empty()){
    int u=stk.top();
    cout<<u<<" ";
    stk.pop();
//loop for traverse
    for(int i=0;i<adj[u].size();i++){
      if(!visit[adj[u][i]]){
        stk.push(adj[u][i]);
        visit[adj[u][i]]=true;
      }
    }
  }
}
//main function
int main(){
    
int n;
cout<<"Enter no.of vertices:"<<endl;
cin>>n;

  vector<int>adj[n];//vector of array to store the graph
  bool visit[n];//array to check visit or not of a node
  //initially all node are unvisited
  for(int i=0;i<n;i++){
    visit[i]=false;
  }
  cout<<"Enter no.of edges:"<<endl;
  int ed1;
  cin>>ed1;
  int v1,v2,ch;
  
  for(int i=0;i<ed1;i++)
  {
      cout<<"Enter starting vertex of edge "<<i+1<<":-"<<endl;
      cin>>v1;
      cout<<"Enter end vertex of edge "<<i+1<<":-"<<endl;
      cin>>v2;
       edge(adj,v1,v2);
  }


  do{
        cout<<"\n\n==========";
        cout<<"\n 1. BFS";
        cout<<"\n 2. DFS";
        cout<<"\n 3. Exit";
        cout<<"\n==========";   
        cout<<"\n\nEnter ur choice : ";
        
        cin>>ch;
        switch(ch)
        {
            case 0:
                exit(1);
                break;
            case 1:
                bfs(0,adj,visit);
                cout<<endl;
                for(int i=0;i<n;i++){
                   visit[i]=false;
                }
                break;
            case 2:
               cout<<"DFS traversal is"<<"  ";
                dfs(0,adj,visit);
               for(int i=0;i<n;i++){
                    visit[i]=false;
                }
                break;
            case 3:
                exit(1);
                break;
            default:
            cout<<"Invalid choice\n";
        }
    }while(ch!=3);
}


