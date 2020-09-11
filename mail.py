import poplib

mailbox = poplib.POP3('smart.whoismail.net', 110)
mailbox.user('dhkim@aisbiz.co.kr')
mailbox.pass_('1Qwe5094*')

print(mailbox.stat()[0], 'count')
mailbox.quit()
