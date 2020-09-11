import poplib

mailbox = poplib.POP3('host', 110)
mailbox.user('user')
mailbox.pass_('password')

print(mailbox.stat()[0], 'count')
mailbox.quit()
