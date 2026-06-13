# Every valid email consists of a local name and a domain name, separated by the '@' sign.
# In the local name, periods '.' are ignored and any substring after a plus '+' is ignored.
# Return the number of unique email addresses.


# Example 1:

# Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2


# Example 2:

# Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
# Output: 3


# Constraints:

# 1 <= emails.length <= 100
# 1 <= emails[i].length <= 100
# emails[i] contain lowercase letters, '+', '.', and exactly one '@'.


class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        seen = set()

        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            seen.add(local + '@' + domain)

        return len(seen)
