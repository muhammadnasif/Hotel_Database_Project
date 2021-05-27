from django.db import connection
from django.shortcuts import render, redirect


# Create your views here.

def load(request):
    context = {
        'save': False
    }
    if request.method == "POST" and 'customer_submit' in request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        nid = request.POST['nid']
        address = request.POST['address']
        company_name = request.POST['company_name']

        sql = "INSERT INTO CUSTOMER VALUES(%s,%s,%s,%s,%s)"
        cursor = connection.cursor()
        cursor.execute(sql, [name, phone, nid, address, company_name])
        connection.commit()
        cursor.close()



    elif request.method == "POST" and 'customer_search' in request.POST:
        phone = request.POST['phone']
        context['save'] = True
        sql = "SELECT * FROM CUSTOMER WHERE PHONE='" + phone + "'"
        cursor = connection.cursor()
        cursor.execute(sql)
        customer = cursor.fetchall()
        cursor.close()
        if len(customer) == 0:
            context['customer'] = {
                'phone': phone
            }
        else:
            for data in customer:
                row = {
                    'name': data[0],
                    'phone': data[1],
                    'nid': data[2],
                    'address': data[3],
                    'company': data[4]
                }
                context['customer'] = row
                break
    print(context)
    return render(request, 'entryForm.html', context)
