# from django.contrib.auth.forms import 
from attr import fields
from django import forms
from games.models import *

####################################################################################################

class XASGroupForm(forms.ModelForm):
    '''For the Umpire to create or edit Groups.'''
    class Meta:
        model = XASGroup
        fields = ['reference']    

####################################################################################################

class FlagForm(forms.ModelForm):
    '''For the Umpire to create or edit Flags.'''
    class Meta:
        model = Flag
        fields = "__all__" 

####################################################################################################

class ConfigScriptForm(forms.ModelForm):
    '''For the Umpire to create or edit Configs.'''
    class Meta:
        model = ConfigScript
        fields = "__all__" 

####################################################################################################

class EventScriptForm(forms.ModelForm):
    '''For the Umpire to create or edit Events.'''
    class Meta:
        model = EventScript
        fields = "__all__" 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['event_start'].widget.attrs['placeholder'] = 'd hh:mm:ss'
        self.fields['event_duration'].widget.attrs['placeholder'] = 'd hh:mm:ss'

####################################################################################################

class GameScriptForm(forms.ModelForm):
    '''For the Umpire to create or edit Scripts.'''
    class Meta:
        model = GameScript
        fields = "__all__" 

    event_scripts = forms.ModelMultipleChoiceField(
        queryset=EventScript.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': "form_multichoice"})
    )

####################################################################################################

class GameForm(forms.ModelForm):
    '''For the Umpire to create or edit Games.'''
    class Meta:
        model = Game
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['game_start'].widget.attrs['placeholder'] = 'yyyy-mm-dd hh:mm:ss'
        self.fields['game_duration'].widget.attrs['placeholder'] = 'd hh:mm:ss'

####################################################################################################

class PlayerForm(forms.ModelForm):
    '''For the Umpire to edit Players in-game.'''
    class Meta:
        model = Player
        fields = "__all__" 
    
    flags = forms.ModelMultipleChoiceField(
        queryset=Flag.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': "form_multichoice"})
    )

####################################################################################################

class DirectReportKillForm(forms.ModelForm):
    '''For a Player to submit or edit a kill report in-game.'''
    class Meta:
        model = DirectReport
        fields = ['victim', 'weapon', 'context', 'location', 'kill_date', 'killer_report'] 

####################################################################################################

class DirectReportDeathForm(forms.ModelForm):
    '''For a Player to submit or edit a death report in-game.'''
    class Meta:
        model = DirectReport
        fields = ['killer', 'weapon', 'context', 'location', 'kill_date', 'victim_report'] 

####################################################################################################

class DirectReportConfirmKillForm(forms.ModelForm):
    '''For a Player to confirm a kill report in-game.'''
    class Meta:
        model = DirectReport
        read_only_fields = ['killer', 'weapon', 'context', 'location', 'kill_date', 'killer_report'] 
        fields = ['victim_report'] 

####################################################################################################

class DirectReportDeathForm(forms.ModelForm):
    '''For a Player to submit or edit a death report in-game.'''
    class Meta:
        model = DirectReport
        read_only_fields = ['victim', 'weapon', 'context', 'location', 'kill_date', 'victim_report'] 
        fields = ['killer_report'] 

####################################################################################################

class IndirectReportSetForm(forms.ModelForm):
    '''For a Player to submit or edit a Indirect-Setting report in-game.'''
    class Meta:
        model = IndirectReport
        fields = ['target', 'location', 'date_set', 'trapper_report']

####################################################################################################

class IndirectReportSpringForm(forms.ModelForm):
    '''For a Player to submit or edit a Indirect-Springing report in-game.'''
    class Meta:
        model = IndirectReport
        read_only_fields = fields = ['trapper', 'location', 'date_set', 'trapper_report']
        fields = ['target_report', 'trap_successful']

####################################################################################################

class GeneralReportForm(forms.ModelForm):
    '''For a Player to submit or edit general report in-game.'''
    class Meta:
        model = GeneralReport
        fields = ['location', 'date', 'report_text']

####################################################################################################

class PlayerBonusForm(forms.ModelForm):
    '''For the Umpire to submit or edit a bonus given to a player in-game.'''
    class Meta:
        model = PlayerBonus
        fields = "__all__" 

####################################################################################################

class FlagBonusForm(forms.ModelForm):
    '''For the Umpire to submit or edit a bonus given to a flag in-game.'''
    class Meta:
        model = FlagBonus
        fields = "__all__" 

####################################################################################################