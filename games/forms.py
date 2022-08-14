from django import forms
from games.models import *

####################################################################################################
############################################ Game Setup ############################################
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

class InfoLoreForm(forms.ModelForm):
    '''For the Umpire to create or edit info/lore releases.'''
    class Meta:
        model = InfoLore
        fields = "__all__" 

    flags = forms.ModelMultipleChoiceField(
        queryset=Flag.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': "form_multichoice"})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['release_start'].widget.attrs['placeholder'] = 'd hh:mm:ss'
        self.fields['release_end'].widget.attrs['placeholder'] = 'd hh:mm:ss'

####################################################################################################

class ConfigScriptForm(forms.ModelForm):
    '''For the Umpire to create or edit Configs.'''
    class Meta:
        model = ConfigScript
        fields = "__all__" 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['respawn_time'].widget.attrs['placeholder'] = 'd hh:mm:ss'
        self.fields['respawn_delay'].widget.attrs['placeholder'] = 'd hh:mm:ss'

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
    info_lore_releases = forms.ModelMultipleChoiceField(
        queryset=InfoLore.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': "form_multichoice"})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['report_deadline'].widget.attrs['placeholder'] = 'd hh:mm:ss'

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
######################################### in-game umpiring #########################################
####################################################################################################

# TODO Implement PlayerForm in a view
class PlayerForm(forms.ModelForm):
    '''For the Umpire to edit Players in-game.'''
    class Meta:
        model = Player
        fields = "__all__" 
    
    flags = forms.ModelMultipleChoiceField(
        queryset=Flag.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': "form_multichoice"})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['next_respawn'].widget.attrs['placeholder'] = 'yyyy-mm-dd hh:mm:ss'

####################################################################################################

# TODO Implement DirectReportForm in a view
class DirectReportForm(forms.ModelForm):
    '''For the Umpire to edit a kill/death report in-game.'''
    class Meta:
        model = DirectReport
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kill_date'].widget.attrs['placeholder'] = 'yyyy-mm-dd hh:mm:ss'
        self.fields['confirm_date'].widget.attrs['placeholder'] = 'yyyy-mm-dd hh:mm:ss'

####################################################################################################

# TODO Implement IndirectReportForm in a view
class IndirectReportForm(forms.ModelForm):
    '''For the Umpire to edit an indirect report in-game.'''
    class Meta:
        model = IndirectReport
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_set'].widget.attrs['placeholder'] = 'yyyy-mm-dd hh:mm:ss'
        self.fields['date_sprung'].widget.attrs['placeholder'] = 'yyyy-mm-dd hh:mm:ss'

####################################################################################################

# TODO Implement GeneralReportForm in a view
class GeneralReportForm(forms.ModelForm):
    '''For the Umpire to edit a general report in-game.'''
    class Meta:
        model = GeneralReport
        fields = ['location', 'date', 'report_text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['placeholder'] = 'yyyy-mm-dd hh:mm:ss'

####################################################################################################

# TODO Implement PlayerBonusForm in a view
class PlayerBonusForm(forms.ModelForm):
    '''For the Umpire to submit or edit a bonus given to a player in-game.'''
    class Meta:
        model = PlayerBonus
        fields = "__all__" 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['placeholder'] = 'yyyy-mm-dd hh:mm:ss'

####################################################################################################

# TODO Implement FlagBonusForm in a view
class FlagBonusForm(forms.ModelForm):
    '''For the Umpire to submit or edit a bonus given to a flag in-game.'''
    class Meta:
        model = FlagBonus
        fields = "__all__" 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['placeholder'] = 'yyyy-mm-dd hh:mm:ss'

####################################################################################################

# TODO Implement PlayerBounty in a view
class PlayerBountyForm(forms.ModelForm):
    '''For the Umpire to submit or edit a bounty on a player in-game.'''
    class Meta:
        model = PlayerBounty
        fields = "__all__" 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_set'].widget.attrs['placeholder'] = 'yyyy-mm-dd hh:mm:ss'
        self.fields['date_claimed'].widget.attrs['placeholder'] = 'yyyy-mm-dd hh:mm:ss'


####################################################################################################
########################################## gameplay forms ##########################################
####################################################################################################

# TODO Implement PlayerSignupForm in a view
# TODO Create PlayerSignupForm

# TODO Implement DirectReportKillForm in a view
class DirectReportKillForm(forms.ModelForm):
    '''For a Player to submit or edit a kill report in-game.'''
    class Meta:
        model = DirectReport
        fields = ['victim', 'weapon', 'context', 'location', 'kill_date', 'killer_report'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kill_date'].widget.attrs['placeholder'] = 'yyyy-mm-dd hh:mm:ss'

####################################################################################################

# TODO Implement DirectReportKillForm in a view
class DirectReportKillForm(forms.ModelForm):
    '''For a Player to submit or edit a kill report in-game.'''
    class Meta:
        model = DirectReport
        fields = ['victim', 'weapon', 'context', 'location', 'kill_date', 'killer_report'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kill_date'].widget.attrs['placeholder'] = 'yyyy-mm-dd hh:mm:ss'

####################################################################################################

# TODO Implement DirectReportDeathForm in a view
class DirectReportDeathForm(forms.ModelForm):
    '''For a Player to submit or edit a death report in-game.'''
    class Meta:
        model = DirectReport
        fields = ['killer', 'weapon', 'context', 'location', 'kill_date', 'victim_report'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kill_date'].widget.attrs['placeholder'] = 'yyyy-mm-dd hh:mm:ss'

####################################################################################################

# TODO Implement DirectReportConfirmKillForm in a view
class DirectReportConfirmKillForm(forms.ModelForm):
    '''For a Player to confirm a kill report in-game.'''
    class Meta:
        model = DirectReport
        read_only_fields = ['killer', 'weapon', 'context', 'location', 'kill_date', 'killer_report'] 
        fields = ['victim_report'] 

####################################################################################################

# TODO Implement DirectReportDeathForm in a view
class DirectReportConfirmDeathForm(forms.ModelForm):
    '''For a Player to confirm a death report in-game.'''
    class Meta:
        model = DirectReport
        read_only_fields = ['victim', 'weapon', 'context', 'location', 'kill_date', 'victim_report'] 
        fields = ['killer_report'] 

####################################################################################################

# TODO Implement IndirectReportSetForm in a view
class IndirectReportSetForm(forms.ModelForm):
    '''For a Player to submit or edit a Indirect-Setting report in-game.'''
    class Meta:
        model = IndirectReport
        fields = ['target', 'location', 'date_set', 'trapper_report']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_set'].widget.attrs['placeholder'] = 'yyyy-mm-dd hh:mm:ss'

####################################################################################################

# TODO Implement IndirectReportSpringForm in a view
class IndirectReportSpringForm(forms.ModelForm):
    '''For a Player to submit or edit a Indirect-Springing report in-game.'''
    class Meta:
        model = IndirectReport
        read_only_fields = fields = ['trapper', 'location', 'date_set', 'trapper_report']
        fields = ['date_sprung', 'target_report', 'trap_successful']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_sprung'].widget.attrs['placeholder'] = 'yyyy-mm-dd hh:mm:ss'

####################################################################################################

# TODO Implement GeneralReportSubmitForm in a view
class GeneralReportSubmitForm(forms.ModelForm):
    '''For a Player to submit or edit general report in-game.'''
    class Meta:
        model = GeneralReport
        fields = ['location', 'date', 'report_text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['placeholder'] = 'yyyy-mm-dd hh:mm:ss'

####################################################################################################