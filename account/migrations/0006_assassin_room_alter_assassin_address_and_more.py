# Generated by Django 4.0.3 on 2022-07-17 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_assassin_address_alter_assassin_startyear_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assassin',
            name='room',
            field=models.CharField(default='1', max_length=256, verbose_name='accomodation room'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assassin',
            name='address',
            field=models.CharField(max_length=256, verbose_name='accomodation address'),
        ),
        migrations.AlterField(
            model_name='assassin',
            name='college',
            field=models.CharField(choices=[('ALL', 'All Souls College'), ('BAL', 'Balliol College'), ('BLA', 'Blackfriars'), ('BRA', 'Brasenose College'), ('CAM', 'Campion Hall'), ('CHR', 'Christ Church'), ('COR', 'Corpus Christi College'), ('EXE', 'Exeter College'), ('GRE', 'Green Templeton College'), ('HAR', 'Harris Manchester College'), ('HER', 'Hertford College'), ('JES', 'Jesus College'), ('KEB', 'Keble College'), ('KEL', 'Kellogg College'), ('LMH', 'Lady Margaret Hall'), ('LNA', 'Linacre College'), ('LNC', 'Lincoln College'), ('MAG', 'Magdalen College'), ('MAN', 'Mansfield College'), ('MER', 'Merton College'), ('NEW', 'New College'), ('NUF', 'Nuffield College'), ('ORI', 'Oriel College'), ('PEM', 'Pembroke College'), ('QUE', "The Queen's College"), ('REG', "Regent's Park College"), ('REU', 'Reuben College'), ('SOM', 'Somerville College'), ('ANN', "St Anne's College"), ('ANT', "St Antony's College"), ('BEN', "St Benet's Hall"), ('CAT', "St Catherine's College"), ('CRO', 'St Cross College'), ('EDM', 'St Edmund Hall'), ('HIL', "St Hilda's College"), ('HUG', "St Hugh's College"), ('JOH', "St John's College"), ('PET', "St Peter's College"), ('STE', "St Stephen's House"), ('TRI', 'Trinity College'), ('UNI', 'University College'), ('WAD', 'Wadham College'), ('WOL', 'Wolfson College'), ('WOR', 'Worcester College'), ('WYC', 'Wycliffe Hall')], max_length=3, verbose_name='college'),
        ),
        migrations.AlterField(
            model_name='assassin',
            name='discordName',
            field=models.CharField(max_length=32, verbose_name='discord name'),
        ),
        migrations.AlterField(
            model_name='assassin',
            name='discordTag',
            field=models.PositiveSmallIntegerField(verbose_name='discord tag'),
        ),
        migrations.AlterField(
            model_name='assassin',
            name='startYear',
            field=models.PositiveSmallIntegerField(verbose_name='year matriculated'),
        ),
        migrations.AlterField(
            model_name='assassin',
            name='subject',
            field=models.CharField(choices=[('ARC', 'UG - Archaeology and Anthropology'), ('BCM', 'UG - Biochemistry (Molecular and Cellular)'), ('BIO', 'UG - Biology'), ('BMS', 'UG - Biomedical Sciences'), ('CHM', 'UG - Chemistry'), ('CAR', 'UG - Classical Archaeology and Ancient History'), ('CLS', 'UG - Classics'), ('CLE', 'UG - Classics and English'), ('CLM', 'UG - Classics and Modern Languages'), ('CLO', 'UG - Classics and Oriental Studies'), ('CSC', 'UG - Computer Science'), ('CSP', 'UG - Computer Science and Philosophy'), ('ESC', 'UG - Earth Sciences (Geology)'), ('ECM', 'UG - Economics and Management'), ('ENG', 'UG - Engineering Science'), ('ELL', 'UG - English Language and Literature'), ('EML', 'UG - English and Modern Languages'), ('EME', 'UG - European and Middle Eastern Languages'), ('FAR', 'UG - Fine Art'), ('FCE', 'UG - Foundation Year (Chemistry, Engineering and Materials Science)'), ('FHU', 'UG - Foundation Year (Humanities)'), ('FLA', 'UG - Foundation Year (Law)'), ('FPP', 'UG - Foundation Year (PPE)'), ('GEO', 'UG - Geography'), ('HIS', 'UG - History'), ('HAM', 'UG - History (Ancient and Modern)'), ('HEC', 'UG - History and Economics'), ('HEN', 'UG - History and English'), ('HML', 'UG - History and Modern Languages'), ('HPO', 'UG - History and Politics'), ('HAR', 'UG - History of Art'), ('HSC', 'UG - Human Sciences'), ('LAW', 'UG - Law (Jurisprudence)'), ('MAS', 'UG - Materials Science'), ('MAT', 'UG - Mathematics'), ('MCS', 'UG - Mathematics and Computer Science'), ('MPH', 'UG - Mathematics and Philosophy'), ('MST', 'UG - Mathematics and Statistics'), ('MED', 'UG - Medicine'), ('MLA', 'UG - Modern Languages'), ('MLL', 'UG - Modern Languages and Linguistics'), ('MUS', 'UG - Music'), ('ORI', 'UG - Oriental Studies'), ('PHL', 'UG - Philosophy and Modern Languages'), ('PHE', 'UG - Philosophy, Politics and Economics (PPE)'), ('PHT', 'UG - Philosophy and Theology'), ('PHY', 'UG - Physics'), ('PHP', 'UG - Physics and Philosophy'), ('PSE', 'UG - Psychology (Experimental)'), ('PSP', 'UG - Psychology, Philosophy and Linguistics'), ('ROR', 'UG - Religion and Oriental Studies'), ('THR', 'UG - Theology and Religion'), ('PGD', 'PG - PGDip'), ('PGC', 'PG - PGCert'), ('BCL', 'PG - BCL'), ('BMB', 'PG - BM BCh'), ('DTP', 'PG - BBSRC DTP'), ('CDT', 'PG - EPSRC CDT'), ('MBA', 'PG - MBA'), ('MFA', 'PG - MFA'), ('MJR', 'PG - MJur'), ('MPH', 'PG - MPhil'), ('MPP', 'PG - MPP'), ('MSC', 'PG - MSc'), ('MST', 'PG - MSt'), ('MTH', 'PG - MTh'), ('DCP', 'PG - DClinPsych'), ('DEN', 'PG - DEng'), ('DPH', 'PG - DPhil')], max_length=3, verbose_name='subject'),
        ),
    ]