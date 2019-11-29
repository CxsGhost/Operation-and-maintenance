import requests

url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=18029102_3_dg&wd=%E5%91%9C%E5%91%9C%E5%91%9C%E5%92%8B%E5%B0%B1%E7%9B%B4%E6%8E%A5%E4%B8%8Aflask%E4%BA%86&rsv_pq=cf79eb0d0008b4f5&rsv_t=bb0cSR9Zhd7Mxi4Tfh1HMXFP%2FpeP2F2Oc%2BjTZq0HTGCGoyB5l0ypyoUWM0B05MduWYFaGg&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=33&rsv_sug1=20&rsv_sug7=101&rsv_sug2=0&inputT=25701&rsv_sug4=43651&rsv_sug=9"
head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"}
html=requests.get(url,headers=head)

html_file=open("百度.txt","w",encoding="utf-8")
html_file.write(html.text)
html_file.close()


