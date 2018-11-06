#参考https://www.jianshu.com/p/4e39444d5ebc
#导入excel库
import xlwt
#导入时间库
import datetime

#创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')

#创建一个worksheet
worksheet = workbook.add_sheet("My sheet")

#写入excel
#行、列、值
worksheet.write(0,0,label = '第0行0列')
worksheet.write(1,0,label = '第1行0列')
worksheet.write(1,1,label = '第1行1列')

#设置单元格宽度，第0列宽度5000
worksheet.col(1).width = 5000

#第一行第一列插入一个日期
style = xlwt.XFStyle()
# Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0
style.num_format_str = 'M/D/YY h:mm'
worksheet.write(0,1,datetime.datetime.now(),style)

workbook.save('Sample.xls')