from dormitory_electricity import *
import json,time
import matplotlib.pyplot as plt

history_file_name="history.json"
result_pic_name="result.png"

def draw_elec_degree():
    elec_history=None
    t=time.localtime()
    try:
        with open(history_file_name,"r",encoding="utf-8") as _f:
            elec_history=json.loads(_f.read())
    except:
        elec_history=[]
    if(len(elec_history)>480):
        elec_history.pop(0)
    
    elec_degree=get_elec_degree()
    if elec_degree != None:
        elec_history.append([elec_degree,f"{t.tm_mon}-{t.tm_mday} {t.tm_hour}:{t.tm_min}"])
        print(f"[{t.tm_mon}-{t.tm_mday} {t.tm_hour}:{t.tm_min}]Successfully fetched elec info: {elec_degree} degrees.")
    else:
        exit(1)

    plt.figure(figsize=(10,3))
    plt.style.use("ggplot")
    plt.plot([i[1] for i in elec_history],[i[0] for i in elec_history])
    plt.title("Dormitory Electricity Tracer")
    plt.xticks(ticks=list(range(0,len(elec_history),10)),rotation=90)
    for i in range(0,len(elec_history),10):
        plt.text(elec_history[i][1],elec_history[i][0],elec_history[i][0],va="top",ha="right",rotation=75)
    plt.tight_layout()
    plt.savefig(result_pic_name)

    with open(history_file_name,"w",encoding="utf-8") as _f:
        _f.write(json.dumps(elec_history))


if __name__ == "__main__":
    draw_elec_degree()