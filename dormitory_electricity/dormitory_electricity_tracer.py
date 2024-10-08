from dormitory_electricity import *
import json,time
import matplotlib.pyplot as plt

history_file_name="history.json"
result_pic_name="result.png"
elec_fee=1.824

def draw_elec_degree():
    elec_history=None
    # [time,degree,diff]
    t=time.localtime()
    try:
        with open(history_file_name,"r",encoding="utf-8") as _f:
            elec_history=json.loads(_f.read())
    except:
        elec_history=[]
    if(len(elec_history)>720):
        elec_history.pop(0)
    
    elec_degree=get_elec_degree()
    if elec_degree != None:
        elec_degree=float(format(elec_degree*elec_fee,".2f"))
        elec_diff=0
        if len(elec_history)>1:
            elec_diff=float(format(elec_history[-1][1]-elec_degree,".4f"))
        elec_history.append([f"{t.tm_mon}-{t.tm_mday} {t.tm_hour}:{t.tm_min}",elec_degree,elec_diff])
        print(f"[{t.tm_mon}-{t.tm_mday} {t.tm_hour}:{t.tm_min}]Successfully fetched elec info: {elec_degree} degrees.")
    else:
        print("Fetch elec info FAILED.")

    plt.figure(figsize=(15,4))
    #plt.style.use("ggplot")
    fig,plt_degree=plt.subplots()
    plt.xticks(ticks=list(range(0,len(elec_history),10)),rotation=90)
    plt_degree.plot([i[0] for i in elec_history],[i[1] for i in elec_history],"g-")
    plt_degree.set_ylabel('Degrees remaining', color='g')
	
    plt_diff=plt_degree.twinx()
    plt_diff.plot([i[0] for i in elec_history],[i[2] for i in elec_history],"b-")
    plt_diff.set_ylabel("Diff",color='b')

    plt.title("Dormitory Electricity Tracer")
    for i in range(0,len(elec_history),10):
        plt_degree.text(elec_history[i][0],elec_history[i][1],elec_history[i][1],va="bottom",ha="left",rotation=75)
        plt_diff.text(elec_history[i][0],elec_history[i][2],elec_history[i][2],va="bottom",ha="left",rotation=75)
    plt.tight_layout()
    plt.savefig(result_pic_name)

    with open(history_file_name,"w",encoding="utf-8") as _f:
        _f.write(json.dumps(elec_history))


if __name__ == "__main__":
    draw_elec_degree()