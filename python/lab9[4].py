prices ={'apple':50,'kiwi':180,'milk':60,'bread':20}
quantities={'apple':12,'kiwi':5,'milk':6,'bread':2}
total_bill=sum(prices[item]*quantities.get(item,0) for item in prices)
print("total bill:",total_bill)
