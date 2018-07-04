import java.io.*;
import java.util.*;
public class Ds
{
public static void main(String args[]) 
{
String str="mom";
char[] text = new char[str.length()]; 
int l,i,count=0,mid,j;
l=str.length();
for(i=0;i<l;i++)
{
for(j=1;j<l;j++)
{
if(text[i]==text[j])
{
count=count+2;
}
}
}
mid=(l/2);
for(i=mid-1;i<=0;i--)
{
for(j=mid+1;j>=l;j++)
{
if(text[i]==text[j])
{
count=count+1;
}
}
}
System.out.println("the number of occurances are"+count);
}
}

