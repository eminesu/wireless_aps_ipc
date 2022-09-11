import multiprocessing
import json
import time
from get_wireless_APs import get_wireless_APs

q=multiprocessing.Queue()


def detect_changes(q):
   get_wireless_APs()

   while True:
      with open('access_points.json', 'r') as openfile:
         try:
            records = json.load(openfile)['access_points']
         except json.decoder.JSONDecodeError:
            records=[]

      get_wireless_APs()

      with open('access_points.json', 'r') as openfile:
         # Reading from json file
         file_changed = json.load(openfile)['access_points']

      if records != file_changed:
         
         ssids = [s['ssid'] for s in file_changed]
         snrs = [n['snr'] for n in file_changed]

         ssids_records = [s_rec['ssid'] for s_rec in records]
         snrs = [n_rec['snr'] for n_rec in records]


         removed = [q.put(x['ssid'] + ' is removed from the list') for x in records if x['ssid'] not in ssids]

         added = [q.put(a['ssid'] + ' is added to the list with SNR ' + a['snr'] + " and channel " + a['channel']) for a in file_changed if a['ssid'] not in ssids_records]
         

         for r in records:
            for c in file_changed:
               if r['ssid'] == c['ssid']:
                  if r['snr'] != c['snr']:
                     q.put(r['ssid'] + "\'s snr value has changed from " + r['snr'] + " to " + c['snr'])
                  if r['channel'] != c['channel']:
                     q.put(r['ssid'] + "\'s channel has changed from " + r['channel'] + " to " + c['channel'])


         time.sleep(10)
      


def print_changes(q):
   while True:
      while not q.empty():
         item = q.get()
         print (item)

      time.sleep(5)

def run_processes():

   with multiprocessing.Manager() as manager:
      p1 = multiprocessing.Process(target = detect_changes, args = (q,))
      p1.daemon=True
      p1.start()
      p2 = multiprocessing.Process(target = print_changes, args = (q,)) 
      p2.daemon=True
      p2.start()
      p1.join()
      p2.join()


if __name__ == '__main__':
   run_processes()
      
