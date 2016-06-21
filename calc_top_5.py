import math

class Helper(object):

  @classmethod
  def cosine_similarity(cls, app_list1, app_list2):
    match_count = cls.__count_match(app_list1, app_list2)
    return float(match_count) / math.sqrt( len(app_list1) * len(app_list2) )

  @classmethod
  def __count_match(cls, list1, list2):
    count = 0
    for element in list1:
      if element in list2:
        count += 1
    return count

