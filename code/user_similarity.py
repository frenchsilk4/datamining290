from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
import itertools

class UserSimilarity(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    ###
    # TODO: write the functions needed to
    # 1) find potential matches, 
    # 2) calculate the Jaccard between users, with a user defined as a set of
    # reviewed businesses
    ##/

    # match_user_toID (self,_,record);
    """ 
    match_user_toID = <_, record> => <userId, business id >
    match_business_to_users = <userId, [list of business id values]> => <business_id, [(userId,scount, (list of each users business ids))]
    (scount is the number of business ids per user)
    match_users_to_business = <business_id, [(user1, scount, [list of user1 biz ids]),[(user2,scount,...)]...]
    combine_pairs_ofusers = <(pair of userId's), Jaccard value)>
    """
    def match_user_toID(self,_,record):
        if record['type'] == 'review':
            bizId = record['business_id']
            userId = record['user_id']
            yield[userId,bizId]

    def match_business_to_users(self,userId,values):
        business_ids = set(values)
        scount = len(business_ids)
        for id in business_ids:
            yield[id,list[userId,scount,list[business_ids]]

    def match_users_to_business(self,busId,userCol):
        usersCollection = list(userCol)
        # {(aisha,4,(a, b, c))}
        i=0
        for col[i] in usersCollection:
            usr = col[0][0]
            bct = col[1][1]
            for col[i+1] in usersCollection:
                unionct += bct + col[i+1][0]
                usr2 = col[i+1][0]

                yield[list[usr,col[i]],[1,unionct]]

    def combine_pairs_ofusers(self,upair,upValues):
        pair_users = set(upair)
        unionlist = list(upValues)
        utotal = unionlist[0][1]

        usrjcd = len(unionlist)/(utotal - (len(unionlist)))
        if(usrjcd > 0.5):
            yield [list(pair_users), usrjcd]

    def steps(self):
        """TODO: Document what you expect each mapper and reducer to produce:
        mapper1: <line, record> => <key, value>
        reducer1: <key, [values]>
        mapper2: ...
        """
        return [self.mr(mapper=self.match_user_toID, reducer=self.match_business_to_users),
                self.mr(mapper=match_users_to_business,reducer=self.combine_pairs_ofusers)]


if __name__ == '__main__':
    UserSimilarity.run()