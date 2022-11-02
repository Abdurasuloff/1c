from django.shortcuts import render, redirect
from .models import Balance, Item, CheckBalance
from .forms import BalanceForm
# Create your views here.

def new_checkbalance(request):
      chekbalance = CheckBalance.objects.create()
      return redirect('/')

def retrieve_checkbalance(request, id):
      balances = Balance.objects.all()
      checkbalance = CheckBalance.objects.get(id=id)
      #print(checkbalance.passives.all())
      #for i in checkbalance.actives.all():
      #      print(i.prize)
      
      if request.method == "POST":
            #Balance Item qo'shish
            b = request.POST['balance']
            balance = Balance.objects.get(id=b)
            price = request.POST['price']
            item = Item.objects.create(balance = balance, prize=price)
            if balance.status == 'active':
                  checkbalance.actives.add(item)
            elif balance.status == 'passiv':
                  checkbalance.passives.add(item)
            else:
                  pass
            #Balanslarni qo'shish
             #avtiklar
            actives = 0
            for i in checkbalance.actives.all():
                  actives += i.prize
                 

              #passivlar      
            passives = 0
            for i in checkbalance.passives.all():
                  passives += i.prize 

            #Tenglikni tekshirish
            is_balanced = False
            if  actives == passives and actives != 0:
                  is_balanced =True
            
            checkbalance.total_actives = actives
            checkbalance.total_passives = passives
            checkbalance.is_balanced = is_balanced
            checkbalance.remainder = actives - passives
            checkbalance.save()

      context = {
            'balances':balances,
            'checkbalance':checkbalance,
      }      
      return  render(request, 'check_balance.html', context)


def delete_balance(request, checkbalance_id, item_id):
      check_balance  = CheckBalance.objects.get(id = checkbalance_id)
      item = Item.objects.get(id=item_id)
    
      if item.balance.status == "active":
            total_actives = check_balance.total_actives - item.prize
            check_balance.total_actives = total_actives
            check_balance.save()
            item = check_balance.actives.get(id = item_id).delete()
            
      elif item.balance.status == "passiv":
            total_passives = check_balance.total_passives - item.prize
            check_balance.total_passives =  total_passives
            check_balance.save()
            item = check_balance.passives.get(id = item_id).delete()
      else:
            print(" Not found")


      return redirect("retrieve", check_balance.id)      


def new_balance(request):
      if request.method == "POST":
            name = request.POST['name']
            code = request.POST['code']
            status = request.POST['status']
            id = request.POST['id']
            Balance.objects.create(
                  name=name,
                  code=code,
                  status=status
            )
            return redirect("retrieve", id)

def index(request):
      checkbalances = CheckBalance.objects.all().order_by('-id')
      return render(request, 'home.html', {'b': checkbalances})
                  
            



