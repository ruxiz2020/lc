from typing import List


class Solution:
  def numUniqueEmails(self, emails: List[str]) -> int:
    seen = set()

    for email in emails:
      local, domain = email.split('@')
      local = local.split('+')[0].replace('.', '')
      seen.add(local + '@' + domain)

    return len(seen)


if __name__ == '__main__':

    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

    ss = Solution()
    res = ss.numUniqueEmails(emails)
    print(res)
