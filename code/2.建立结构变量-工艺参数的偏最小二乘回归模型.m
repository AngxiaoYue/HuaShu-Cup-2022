clc,clear
ab0=load('data1.txt');   
mu=mean(ab0), sig=std(ab0) 
rr=corrcoef(ab0)  
ab=zscore(ab0); 
a=ab(:,[1:2]);b=ab(:,[3:end]);  
[XL,YL,XS,YS,BETA,PCTVAR,MSE,stats] =plsregress(a,b)
contr=cumsum(PCTVAR,2)
xw=a\XS 
yw=b\YS  
ncomp=input('请根据PCTVAR的值确定提出成分对的个数ncomp=');
[XL2,YL2,XS2,YS2,BETA2,PCTVAR2,MSE2,stats2] =plsregress(a,b,ncomp)
n=size(a,2); m=size(b,2);
beta3(1,:)=mu(n+1:end)-mu(1:n)./sig(1:n)*BETA2([2:end],:).*sig(n+1:end); 
beta3([2:n+1],:)=(1./sig(1:n))'*sig(n+1:end).*BETA2([2:end],:) 
yhat=repmat(beta3(1,:),[size(a,1),1])+ab0(:,[1:n])*beta3([2:end],:) 
y0 = ab0(:,end-size(yhat,2)+1:end)
for i =1:size(b,2)
    yz = y0(:,i);
    yc = yhat(:,i);
    N = size(a,1);
    perf = mse(y0,yhat)
    figure;
    plotregression(yz,yc,['第',num2str(i),'个回归图'])
    e = yz-yc;
    figure;
    ploterrhist(e,['第',num2str(i),'个误差直方图'])
    R2 = (N*sum(yc.*yz)-sum(yc)*sum(yz))^2/((N*sum((yc).^2)-(sum(yc))^2)*(N*sum((yz).^2)-(sum(yz))^2)); 
    figure;
    plot(1:N,yz,'b:*',1:N,yc,'r-o')
    legend('真实值','预测值','location','best')
    xlabel('预测样本')
    ylabel('值')
    string = {'因变量预测结果对比';[]};
    title(string)
end   
ymax=max([yhat;ab0(:,[n+1:end])]); %求预测值和观测值的最大值
bar(BETA2','k')   %画直方图
title("偏最小二乘回归系数直方图")
plot(yhat(:,1),ab0(:,n+1),'*',[0:ymax(1)],[0:ymax(1)],'Color','k')
legend('单杠成绩预测图'), xlabel('预测数据'), ylabel('观测数据')
%下面画y1,y2,y3的预测图，并画直线y=x
figure, subplot(2,2,1)
plot(yhat(:,1),ab0(:,n+1),'*',[0:ymax(1)],[0:ymax(1)],'Color','k')
legend('厚度预测图'), xlabel('预测数据'), ylabel('观测数据')
subplot(2,2,2)
plot(yhat(:,2),ab0(:,n+2),'O',[0:ymax(2)],[0:ymax(2)],'Color','k')
legend('孔隙率预测图'), xlabel('预测数据'), ylabel('观测数据')
subplot(2,2,3)
plot(yhat(:,3),ab0(:,end),'H',[0:ymax(3)],[0:ymax(3)],'Color','k')
legend('压缩回弹性预测图'), xlabel('预测数据'), ylabel('观测数据')
