#include <mpi.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


//the function calculate sum of all integers for parallel compute
int sum(int start,int end,int data[])
{
   int x;
   int sump = 0;
   for(x = start;x<end;x++)
     {
	sump+= data[x];
     }
   return sump;
}
//the function calculate frequency of MODE of all integers for parallel compute
int freq_mode(int start,int end,int data[])
{
        int i;
        int j;
        int bench = 0;
        for(i=start;i<end;i++)
       {
   	            int count=0;
	            for(j=0;j<10000;j++)
	    {
	       
	                if(data[j] == data[i])
		 {
		    
		                    count++;
		 }
	       
	    }
 
	       if(count > bench)
	    {
		      bench = count;
	    }
	  
	   
       }
   
   
   return bench;
}
//the function is for finding the MODE of all integers for parallel compute
int mode(int start,int end,int data[],int q)
{   
     int i;
     int j;
     int qb = 0;
    for(i=start;i<end;i++){     
       int count=0;
       for(j=0;j<10000;j++){
	  if(data[j] == data[i])
          {
                count++;
          }
				                 
        }    
     if(count == q)
      {
	qb = data[i];
      }       
       }
   return qb;
}

//the function calculate dot product of half integers and another half for parallel compute
int dot_prod(int start,int end,int data[])
{
   int c;
   int dotproq = 0;
   for(c = start;c<end;c++)
     {
	if(c<5000)
	  {
	     dotproq+= data[c]*data[c+5000];
	  }
	else
	  {
	     return dotproq;
	  }
	
     }
  	 return dotproq;
}

int main(int argc, char** argv) {
  // Initialize the MPI environment
  MPI_Init(NULL, NULL);
  // Get the number of processes
  int world_size;
  int errorcode = -1;
  MPI_Comm_size(MPI_COMM_WORLD, &world_size);
  // Get the rank of the process
    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
  //make the program can only run in 2 or 3 processors
  if (world_size== 1)
  {
  printf("You must run this program with two or three processes\n");
  MPI_Abort(MPI_COMM_WORLD, errorcode);
  }else if (world_size > 3)
  {
  printf("You must run this program with two or three processes\n");
  MPI_Abort(MPI_COMM_WORLD, errorcode);
  }
   
   //read the data file
   int len = 10000;
   int data[len];
   if(world_rank == 0)
      {FILE *fp = fopen("/tmp/assign1/Array.csv","r");
   char a[20921];
   char *result;
	 //this is for finding how much char in the csv file
	// int t;
	// fseek(fp,0L,2);
	// t = ftell(fp);
	// printf("%d",t);
   if(fp == NULL)
     {
	printf("Error\n");
        return -1;
     }
   while(fgets(a,20921,fp)!=NULL)
     {
        result=strtok(a,",");
	int i =0;
	while(result!=NULL)
	  {
	   sscanf(result,"%d",&data[i]);
           i++;
	   result =strtok(NULL,",");  
	  }	
     }
   fclose(fp);
   fp =NULL;
     //below is the calculation on the root processor only
     //calculate all integers from files
	       int sum =0;
	       int x;
	       for(x =0; x<len;x++)
	   {
	          sum+=data[x];
	   }
	 
	 
	       //find the mode of all integers and the frequency of mode
	       int modevalue=0;
	       int modecount=0;
	       int i,j;
	       for(i=0;i<10000;i++)
	   {
	      
	      
	                      int count=0;
	                      for(j=0;j<10000;j++)
		{
		   
		   
		                             if(data[j] == data[i])
		     {
                                    count++;
		}
	      
	                     
	   }
	     
	           
	                 if(count > modecount)
	   {
	      
	                
	                           modevalue = data[i];
	                           modecount = count;
	   }
	 
	           
      }
       
       //Calculate the dot product of the first 5,000 integers and the second 5,000 i$
         int b;
         int dotpro = 0;
         for(b = 0;b<5000;b++)
     {	              
	dotpro+=data[b]*data[b+5000];
     }
   
        
      printf("Below is the result of root processor:\nsum:%d\n",sum);
      printf("mode value:%d\n",modevalue);
      printf("mode frequency:%d\n",modecount);
      printf("dot product:%d\n",dotpro);
      }
   //broadcast the data[] that contains all data from csv file to other processor
   MPI_Bcast(&data,len,MPI_INT,0,MPI_COMM_WORLD);   
   MPI_Barrier(MPI_COMM_WORLD);
   //creat some variables to store the results
   int sump=0;
   int tsum =0;
   int proq=0;
   int prot=0;
   int freq = 0;
   int freqt = 0;
   int mod = 0;
   int modet = 0;
   //devide the task to every proceccer
   //if it can not equally diviede,devide remainder into the front processors so it can nearly equally devide the task no matter how much the processors is. 
   int count = len /world_size;
   int remainder =  len %world_size;
   int start, end;
   int s;
   int z;
   if (world_rank < remainder)     {
	
	start=world_rank*(count+1);
	end = start+count+1;
    }
	else
     {
	start = world_rank*count+remainder;
	end = start+count;
     }
	//start calculate sum and product in seperate processors
	sump = sum(start,end,data);
	proq = dot_prod(start,end,data);   
   //merge all results of different processors and sum them.
  MPI_Reduce(&sump,&tsum,1,MPI_INT,MPI_SUM, 0,MPI_COMM_WORLD);
   MPI_Reduce(&proq,&prot,1,MPI_INT,MPI_SUM, 0,MPI_COMM_WORLD);
//calculate the max frequency and depends on the max frequency to find the mode;
   freq  = freq_mode(start,end,data);
   MPI_Reduce(&freq,&freqt,1,MPI_INT,MPI_MAX, 0,MPI_COMM_WORLD);
   mod  = mode(start,end,data,freqt);
   MPI_Reduce(&mod,&modet,1,MPI_INT,MPI_MAX, 0,MPI_COMM_WORLD);
   if(world_rank== 0)
     {
        printf("Below it the results of parallel computing:\nsum in parallel computing:%d\n",tsum);
        printf("mode in parallel computing:%d\n",modet);
	printf("sequence of mode in parallel computing:%d\n",freqt);
        printf("dot product in parallel computing:%d\n",prot);
	
     }
   
  // Finalize the MPI environment.
    MPI_Finalize();
}
