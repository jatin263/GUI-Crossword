import math
def dis_cal(a,b):
  ans=(((a[0]-b[0])**2)+((a[1]-b[1])**2))**(1/2)
  return ans

def dis_cal_ind(dis_ind):
  dis=[]
  for i in dis_ind:
    s=[]
    g=65+i
    gg=65
    for j in dis_ind:
      ggg=gg+j
      #print(chr(g)+" - > "+chr(ggg))
      s.append([chr(ggg),dis_cal(co[i],co[j])])      
    dis.append(s)
  for i in range(len(dis)):
    for j in range(len(dis[i])):
      for k in range(len(dis[i])):
        if(dis[i][j][1]<dis[i][k][1]):
          temp1=dis[i][j][0]
          temp2=dis[i][j][1]
          dis[i][j][0]=dis[i][k][0]
          dis[i][j][1]=dis[i][k][1]
          dis[i][k][0]=temp1
          dis[i][k][1]=temp2
  return dis

def cal_cluster(dis,maxcapacity):
  jk=[]
  df=[]
  for i in dis:
    ss=""
    gt=0
    for j in range(len(i)-len(i)+maxcapacity):
      ss=ss+i[j][0]
      gt=gt+i[j][1]
    jk.append(ss)
    df.append([ss,gt])
  for i in range(len(df)):
    for j in range(len(df)):
      if df[i][1]<df[j][1]:
        df[i],df[j]=df[j],df[i]
  #for i in df:
  #  print(i)
  print("Cluster is {} with centeroid {}".format(df[0][0],df[0][0][0]))
  return df
  



co=[[-2,2],[-3,2],[-2,3],[-3,3],[1,1],[1,0],[2,1],[0,0],[-3,1],[-2,1],[3,1],[2,0],[2,2],[-4,2],[1,2]]
print(len(co))
no_sensor,maxcapacity=len(co),6
m=math.ceil(no_sensor/maxcapacity)
print(m)
dis_ind=[]
for i in range(0,len(co)):
  dis_ind.append(i)
#print(dis_ind)
#calculating distance between all nodes
outt=""
for i in range(m):
  dis=dis_cal_ind(dis_ind)
  if len(dis)>=maxcapacity:
    outt=outt+cal_cluster(dis,maxcapacity)[0][0]
  else:
    outt=outt+cal_cluster(dis,len(dis))[0][0]
  ddf=[]
  for i in range(65,65+no_sensor):
    if chr(i) not in outt:
      ddf.append(i-65)
  dis_ind = ddf

