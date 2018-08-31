from datetime import datetime

from Config import general as gen_const
from Data import google_sheet as gs
from Util import email_util as em

sheet = gs.fetch(sheet_name="AUTO_NOTIF_GSS_INACTIVITY")
counter = 2

for l in sheet.get_all_records():
    print(l)
    if l['Status'] == 0:
        print('Status is unvisited')
        if (l['Last'] != '' and (datetime.now() - datetime.strptime(l['Last'], gen_const.TIME_STAMP_FORMAT)).days > 30) or l['Last'] == '':
            print(
                'Last sent is over a month ago, Sending email to ' + l['Email'])
            em.compose_and_send(fromaddr="feedback.strategy@gmail.com",
                                frompass='26jan@2018', toaddr=l['Email'], name=l['Name'])
            gs.write(row=counter, column=4,
                     data=datetime.now().strftime(gen_const.TIME_STAMP_FORMAT), sheet=sheet)
            print('Updated timestamp')
        else:
            print('A reminder was sent under a month ago')
    else:
        print('Status is visited')
    counter += 1
