from django.db import models
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver

# Create your models here.

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Player(models.Model):
    Name = models.CharField(max_length = 128,verbose_name = "Write the player's Name")
    Description = models.TextField(max_length = 16384, null = True, blank = True)

    Balls = models.IntegerField(verbose_name = "Total Balls", default = 0)
    Moves = models.IntegerField(verbose_name = "Total Moves", default = 9999)
    Time = models.IntegerField(verbose_name = "Total Time (milliseconds)", default = 99999000)
    # OCDTime = models.IntegerField(verbose_name = "Total OCDTime", null = True, blank = True)

    def __str__(self):
        return self.Name

    def hash(h, key1,key2):
        return h[key1,key2]
    
    class Meta:
        ordering = ["Name"]

class Record(models.Model):
    # RecordInstance
    Available = models.IntegerField(verbose_name = "Write 0 if record is N/A, otherwise 1")
    # If unavailble, will be presented as N/A
    Name = models.CharField(max_length = 128,verbose_name = "Use 'LevelName-Record', *MUST NOT* contain spaces, use dash (-) instead")
    LevelName = models.CharField(max_length = 128,verbose_name = "Copy the EXACT name of LEVEL written on main site, INCLUDING spaces.")
    Player = models.ForeignKey('Player', on_delete = models.SET_NULL, null = True, blank = True, related_name = 'player1')
    Date = models.DateField(null = True, blank = True, verbose_name = "Date Achieved")
    RECORD_TYPE = {
        ("B", "Balls"),
        ("M", "Moves"),
        ("T", "Time"),
        ("O", "OCDTime"),
    }
    Type = models.CharField(
        max_length = 2,
        choices = RECORD_TYPE,
        default = "B",
    )
    Score = models.IntegerField("Score, in *MILLISECONDS* for time records")
    # For time, Score is milliseconds.
    Link = models.URLField(max_length = 256, null = True, blank = True)
    DownloadLink = models.URLField(max_length = 256, null = True, blank = True)
    ImageLink = models.URLField(max_length = 256, null = True, blank = True)
    Description = models.TextField(max_length = 16384, null = True, blank = True, verbose_name = "Player's comments")
    Description_notes = models.TextField(max_length = 16384, null = True, blank = True, verbose_name = "Notes from Website Managers")
    
    def __str__(self):
        return self.Name
    
    class Meta:
        ordering = ["-Date"]


class Record2(models.Model):
    # RecordInstance
    Available = models.IntegerField(verbose_name = "Write 0 if record is N/A, otherwise 1")
    # If unavailble, will be presented as N/A
    BelongLevel = models.ForeignKey('Level2', on_delete = models.SET_NULL, null = True, blank = True, related_name = 'record2')
    Player = models.ForeignKey('Player', on_delete = models.SET_NULL, null = True, blank = True, related_name = 'player2')
    Date = models.DateField(null = True, blank = True, verbose_name = "Date Achieved")
    ExactTime = models.TimeField(null = True, blank = True, verbose_name = "exact time Achieved")

    RECORD_TYPE = {
        ("B", "Balls"),
        ("M", "Moves"),
        ("T", "Time"),
        ("O", "OCDTime"),
    }
    Type = models.CharField(
        max_length = 2,
        choices = RECORD_TYPE,
        default = "B",
    )
    Score = models.IntegerField("Score, in *MILLISECONDS* for time records")
    # For time, Score is milliseconds.
    Link = models.URLField(max_length = 256, null = True, blank = True)
    DownloadLink = models.URLField(max_length = 256, null = True, blank = True)
    ImageLink = models.URLField(max_length = 256, null = True, blank = True)
    Description = models.TextField(max_length = 16384, null = True, blank = True, verbose_name = "Player's comments")
    Description_notes = models.TextField(max_length = 16384, null = True, blank = True, verbose_name = "Notes from Website Managers")

    # Name = models.CharField(max_length = 128,verbose_name = "Use 'LevelName-Record', *MUST NOT* contain spaces, use dash (-) instead")
    # LevelName = models.CharField(max_length = 128,verbose_name = "Copy the EXACT name of LEVEL written on main site, INCLUDING spaces.")
    Name = models.CharField(max_length = 128,null = True,blank = True,verbose_name = "Leave Blank")
    LevelName = models.CharField(max_length = 128,null = True,blank = True,verbose_name = "Leave Blank")

    
    def __str__(self):
        return self.Name
    
    class Meta:
        ordering = ["-Date","-ExactTime"]

@receiver(pre_save, sender = Record2)
def generate_record_name(sender, **kwargs):
    instance = kwargs['instance']
    name = instance.BelongLevel.LevelName
    instance.LevelName = name
    print(name)
    name = name.replace(' ','-')
    print(name)
    name = name.replace('\'','')
    print(name)
    name = name + "-" + str(instance.Score)
    print(name)
    print(instance.Type)
    if instance.Type == "B":
        name = name + "-Balls"
    if instance.Type == "M":
        name = name + "-Moves"
    if instance.Type == "T":
        name = name + "-Milliseconds-Goal"
    instance.Name = name
    print(name)
    
class Level(models.Model):
    # level
    LevelName = models.CharField(max_length = 128)
    LevelId = models.IntegerField()
    Version = models.CharField(max_length = 10,default = "1.3")
    BallRec = models.OneToOneField('Record', on_delete = models.SET_NULL, null = True, blank = True, related_name = 'balls')
    MoveRec = models.OneToOneField('Record', on_delete = models.SET_NULL, null = True, blank = True, related_name = 'moves')
    TimeRec = models.OneToOneField('Record', on_delete = models.SET_NULL, null = True, blank = True, related_name = 'times')
    OCDTimeRec = models.OneToOneField('Record', on_delete = models.SET_NULL, null = True, blank = True, related_name = 'ocdtimes')

    def __str__(self):
        return self.LevelName
    
    class Meta:
        ordering = ["LevelId"]
    
class Level2(models.Model):
    # level
    LevelName = models.CharField(max_length = 128)
    LevelId = models.IntegerField()
    Version = models.CharField(max_length = 10,default = "2.0")
    BallRec = models.OneToOneField('Record2', on_delete = models.SET_NULL, null = True, blank = True, related_name = 'balls')
    MoveRec = models.OneToOneField('Record2', on_delete = models.SET_NULL, null = True, blank = True, related_name = 'moves')
    TimeRec = models.OneToOneField('Record2', on_delete = models.SET_NULL, null = True, blank = True, related_name = 'times')
    OCDTimeRec = models.OneToOneField('Record2', on_delete = models.SET_NULL, null = True, blank = True, related_name = 'ocdtimes')

    def __str__(self):
        return self.LevelName
    
    class Meta:
        ordering = ["LevelId"]