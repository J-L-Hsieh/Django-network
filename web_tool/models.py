# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Gene(models.Model):
    gene_id = models.TextField(db_column='Gene_id', primary_key=True)  # Field name made lowercase.
    transcript_id = models.TextField(db_column='transcript_ID', blank=True, null=True)  # Field name made lowercase.
    numbers = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Gene'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DiseaseAll(models.Model):
    disease = models.TextField(primary_key=True)
    count = models.IntegerField(blank=True, null=True)
    systematicname = models.TextField(db_column='SystematicName', blank=True, null=True)  # Field name made lowercase.
    associated_genetic_interaction = models.TextField(db_column='Associated_genetic_interaction', blank=True, null=True)  # Field name made lowercase.
    associated_go_c = models.TextField(db_column='Associated_go_c', blank=True, null=True)  # Field name made lowercase.
    associated_go_f = models.TextField(db_column='Associated_go_f', blank=True, null=True)  # Field name made lowercase.
    associated_go_p = models.TextField(db_column='Associated_go_p', blank=True, null=True)  # Field name made lowercase.
    associated_pathway = models.TextField(db_column='Associated_pathway', blank=True, null=True)  # Field name made lowercase.
    associated_phenotype = models.TextField(db_column='Associated_phenotype', blank=True, null=True)  # Field name made lowercase.
    associated_physical_interaction = models.TextField(db_column='Associated_physical_interaction', blank=True, null=True)  # Field name made lowercase.
    associated_protein_domain = models.TextField(db_column='Associated_protein_domain', blank=True, null=True)  # Field name made lowercase.
    associated_regulator = models.TextField(db_column='Associated_regulator', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disease_all'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GeneticInteractionAll(models.Model):
    genetic_interaction = models.TextField(primary_key=True)
    count = models.IntegerField(blank=True, null=True)
    systematicname = models.TextField(db_column='SystematicName', blank=True, null=True)  # Field name made lowercase.
    genetic_interaction_1 = models.TextField(db_column='genetic_interaction.1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    associated_disease = models.TextField(db_column='Associated_disease', blank=True, null=True)  # Field name made lowercase.
    associated_go_c = models.TextField(db_column='Associated_go_c', blank=True, null=True)  # Field name made lowercase.
    associated_go_f = models.TextField(db_column='Associated_go_f', blank=True, null=True)  # Field name made lowercase.
    associated_go_p = models.TextField(db_column='Associated_go_p', blank=True, null=True)  # Field name made lowercase.
    associated_pathway = models.TextField(db_column='Associated_pathway', blank=True, null=True)  # Field name made lowercase.
    associated_phenotype = models.TextField(db_column='Associated_phenotype', blank=True, null=True)  # Field name made lowercase.
    associated_physical_interaction = models.TextField(db_column='Associated_physical_interaction', blank=True, null=True)  # Field name made lowercase.
    associated_protein_domain = models.TextField(db_column='Associated_protein_domain', blank=True, null=True)  # Field name made lowercase.
    associated_regulator = models.TextField(db_column='Associated_regulator', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'genetic_interaction_all'


class GoCAll(models.Model):
    go_c = models.TextField(primary_key=True)
    count = models.IntegerField(blank=True, null=True)
    systematicname = models.TextField(db_column='SystematicName', blank=True, null=True)  # Field name made lowercase.
    associated_disease = models.TextField(db_column='Associated_disease', blank=True, null=True)  # Field name made lowercase.
    associated_genetic_interaction = models.TextField(db_column='Associated_genetic_interaction', blank=True, null=True)  # Field name made lowercase.
    associated_go_f = models.TextField(db_column='Associated_go_f', blank=True, null=True)  # Field name made lowercase.
    associated_go_p = models.TextField(db_column='Associated_go_p', blank=True, null=True)  # Field name made lowercase.
    associated_pathway = models.TextField(db_column='Associated_pathway', blank=True, null=True)  # Field name made lowercase.
    associated_phenotype = models.TextField(db_column='Associated_phenotype', blank=True, null=True)  # Field name made lowercase.
    associated_physical_interaction = models.TextField(db_column='Associated_physical_interaction', blank=True, null=True)  # Field name made lowercase.
    associated_protein_domain = models.TextField(db_column='Associated_protein_domain', blank=True, null=True)  # Field name made lowercase.
    associated_regulator = models.TextField(db_column='Associated_regulator', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'go_c_all'


class GoFAll(models.Model):
    go_f = models.TextField(primary_key=True)
    count = models.IntegerField(blank=True, null=True)
    systematicname = models.TextField(db_column='SystematicName', blank=True, null=True)  # Field name made lowercase.
    associated_disease = models.TextField(db_column='Associated_disease', blank=True, null=True)  # Field name made lowercase.
    associated_genetic_interaction = models.TextField(db_column='Associated_genetic_interaction', blank=True, null=True)  # Field name made lowercase.
    associated_go_c = models.TextField(db_column='Associated_go_c', blank=True, null=True)  # Field name made lowercase.
    associated_go_p = models.TextField(db_column='Associated_go_p', blank=True, null=True)  # Field name made lowercase.
    associated_pathway = models.TextField(db_column='Associated_pathway', blank=True, null=True)  # Field name made lowercase.
    associated_phenotype = models.TextField(db_column='Associated_phenotype', blank=True, null=True)  # Field name made lowercase.
    associated_physical_interaction = models.TextField(db_column='Associated_physical_interaction', blank=True, null=True)  # Field name made lowercase.
    associated_protein_domain = models.TextField(db_column='Associated_protein_domain', blank=True, null=True)  # Field name made lowercase.
    associated_regulator = models.TextField(db_column='Associated_regulator', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'go_f_all'


class GoPAll(models.Model):
    go_p = models.TextField(primary_key=True)
    count = models.IntegerField(blank=True, null=True)
    systematicname = models.TextField(db_column='SystematicName', blank=True, null=True)  # Field name made lowercase.
    associated_disease = models.TextField(db_column='Associated_disease', blank=True, null=True)  # Field name made lowercase.
    associated_genetic_interaction = models.TextField(db_column='Associated_genetic_interaction', blank=True, null=True)  # Field name made lowercase.
    associated_go_c = models.TextField(db_column='Associated_go_c', blank=True, null=True)  # Field name made lowercase.
    associated_go_f = models.TextField(db_column='Associated_go_f', blank=True, null=True)  # Field name made lowercase.
    associated_pathway = models.TextField(db_column='Associated_pathway', blank=True, null=True)  # Field name made lowercase.
    associated_phenotype = models.TextField(db_column='Associated_phenotype', blank=True, null=True)  # Field name made lowercase.
    associated_physical_interaction = models.TextField(db_column='Associated_physical_interaction', blank=True, null=True)  # Field name made lowercase.
    associated_protein_domain = models.TextField(db_column='Associated_protein_domain', blank=True, null=True)  # Field name made lowercase.
    associated_regulator = models.TextField(db_column='Associated_regulator', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'go_p_all'


class PathwayAll(models.Model):
    pathway = models.TextField(primary_key=True)
    count = models.IntegerField(blank=True, null=True)
    systematicname = models.TextField(db_column='SystematicName', blank=True, null=True)  # Field name made lowercase.
    associated_disease = models.TextField(db_column='Associated_disease', blank=True, null=True)  # Field name made lowercase.
    associated_genetic_interaction = models.TextField(db_column='Associated_genetic_interaction', blank=True, null=True)  # Field name made lowercase.
    associated_go_c = models.TextField(db_column='Associated_go_c', blank=True, null=True)  # Field name made lowercase.
    associated_go_f = models.TextField(db_column='Associated_go_f', blank=True, null=True)  # Field name made lowercase.
    associated_go_p = models.TextField(db_column='Associated_go_p', blank=True, null=True)  # Field name made lowercase.
    associated_phenotype = models.TextField(db_column='Associated_phenotype', blank=True, null=True)  # Field name made lowercase.
    associated_physical_interaction = models.TextField(db_column='Associated_physical_interaction', blank=True, null=True)  # Field name made lowercase.
    associated_protein_domain = models.TextField(db_column='Associated_protein_domain', blank=True, null=True)  # Field name made lowercase.
    associated_regulator = models.TextField(db_column='Associated_regulator', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pathway_all'


class PhenotypeAll(models.Model):
    phenotype = models.TextField(primary_key=True)
    count = models.IntegerField(blank=True, null=True)
    systematicname = models.TextField(db_column='SystematicName', blank=True, null=True)  # Field name made lowercase.
    associated_disease = models.TextField(db_column='Associated_disease', blank=True, null=True)  # Field name made lowercase.
    associated_genetic_interaction = models.TextField(db_column='Associated_genetic_interaction', blank=True, null=True)  # Field name made lowercase.
    associated_go_c = models.TextField(db_column='Associated_go_c', blank=True, null=True)  # Field name made lowercase.
    associated_go_f = models.TextField(db_column='Associated_go_f', blank=True, null=True)  # Field name made lowercase.
    associated_go_p = models.TextField(db_column='Associated_go_p', blank=True, null=True)  # Field name made lowercase.
    associated_pathway = models.TextField(db_column='Associated_pathway', blank=True, null=True)  # Field name made lowercase.
    associated_physical_interaction = models.TextField(db_column='Associated_physical_interaction', blank=True, null=True)  # Field name made lowercase.
    associated_protein_domain = models.TextField(db_column='Associated_protein_domain', blank=True, null=True)  # Field name made lowercase.
    associated_regulator = models.TextField(db_column='Associated_regulator', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'phenotype_all'


class PhysicalInteractionAll(models.Model):
    physical_interaction = models.TextField(primary_key=True)
    count = models.IntegerField(blank=True, null=True)
    systematicname = models.TextField(db_column='SystematicName', blank=True, null=True)  # Field name made lowercase.
    associated_disease = models.TextField(db_column='Associated_disease', blank=True, null=True)  # Field name made lowercase.
    associated_genetic_interaction = models.TextField(db_column='Associated_genetic_interaction', blank=True, null=True)  # Field name made lowercase.
    associated_go_c = models.TextField(db_column='Associated_go_c', blank=True, null=True)  # Field name made lowercase.
    associated_go_f = models.TextField(db_column='Associated_go_f', blank=True, null=True)  # Field name made lowercase.
    associated_go_p = models.TextField(db_column='Associated_go_p', blank=True, null=True)  # Field name made lowercase.
    associated_pathway = models.TextField(db_column='Associated_pathway', blank=True, null=True)  # Field name made lowercase.
    associated_phenotype = models.TextField(db_column='Associated_phenotype', blank=True, null=True)  # Field name made lowercase.
    associated_protein_domain = models.TextField(db_column='Associated_protein_domain', blank=True, null=True)  # Field name made lowercase.
    associated_regulator = models.TextField(db_column='Associated_regulator', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'physical_interaction_all'


class ProteinDomainAll(models.Model):
    protein_domain = models.TextField(primary_key=True)
    count = models.IntegerField(blank=True, null=True)
    systematicname = models.TextField(db_column='SystematicName', blank=True, null=True)  # Field name made lowercase.
    associated_disease = models.TextField(db_column='Associated_disease', blank=True, null=True)  # Field name made lowercase.
    associated_genetic_interaction = models.TextField(db_column='Associated_genetic_interaction', blank=True, null=True)  # Field name made lowercase.
    associated_go_c = models.TextField(db_column='Associated_go_c', blank=True, null=True)  # Field name made lowercase.
    associated_go_f = models.TextField(db_column='Associated_go_f', blank=True, null=True)  # Field name made lowercase.
    associated_go_p = models.TextField(db_column='Associated_go_p', blank=True, null=True)  # Field name made lowercase.
    associated_pathway = models.TextField(db_column='Associated_pathway', blank=True, null=True)  # Field name made lowercase.
    associated_phenotype = models.TextField(db_column='Associated_phenotype', blank=True, null=True)  # Field name made lowercase.
    associated_physical_interaction = models.TextField(db_column='Associated_physical_interaction', blank=True, null=True)  # Field name made lowercase.
    associated_regulator = models.TextField(db_column='Associated_regulator', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'protein_domain_all'


class RegulatorAll(models.Model):
    regulator = models.TextField(primary_key=True)
    count = models.IntegerField(blank=True, null=True)
    systematicname = models.TextField(db_column='SystematicName', blank=True, null=True)  # Field name made lowercase.
    associated_disease = models.TextField(db_column='Associated_disease', blank=True, null=True)  # Field name made lowercase.
    associated_genetic_interaction = models.TextField(db_column='Associated_genetic_interaction', blank=True, null=True)  # Field name made lowercase.
    associated_go_c = models.TextField(db_column='Associated_go_c', blank=True, null=True)  # Field name made lowercase.
    associated_go_f = models.TextField(db_column='Associated_go_f', blank=True, null=True)  # Field name made lowercase.
    associated_go_p = models.TextField(db_column='Associated_go_p', blank=True, null=True)  # Field name made lowercase.
    associated_pathway = models.TextField(db_column='Associated_pathway', blank=True, null=True)  # Field name made lowercase.
    associated_phenotype = models.TextField(db_column='Associated_phenotype', blank=True, null=True)  # Field name made lowercase.
    associated_physical_interaction = models.TextField(db_column='Associated_physical_interaction', blank=True, null=True)  # Field name made lowercase.
    associated_protein_domain = models.TextField(db_column='Associated_protein_domain', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'regulator_all'


class TranscriptWbidType(models.Model):
    index = models.AutoField(primary_key=True)
    transcript = models.TextField(blank=True, null=True)
    wormbase_id = models.TextField(db_column='Wormbase_id', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transcript_wbid_type'


class WebToolGene(models.Model):
    gene_id = models.CharField(max_length=100)
    transcript_id = models.CharField(max_length=100)
    numbers = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'web_tool_gene'


class WebToolUser(models.Model):
    user_name = models.CharField(primary_key=True, max_length=100)
    user_password = models.CharField(max_length=100)
    user_content = models.TextField()

    class Meta:
        managed = False
        db_table = 'web_tool_user'


class Wormbase(models.Model):
    wormbase_id = models.TextField(db_column='WormBase ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    sequence_name = models.TextField(db_column='Sequence Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gene_name = models.TextField(db_column='Gene Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    other_name = models.TextField(db_column='Other Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'wormbase'


class WormbaseGenetranscriptW285(models.Model):
    wormbase_id = models.TextField(db_column='WormBase_ID', primary_key=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    sequence_name = models.TextField(db_column='Sequence_Name', blank=True, null=True)  # Field name made lowercase.
    gene_name = models.TextField(db_column='Gene_Name', blank=True, null=True)  # Field name made lowercase.
    other_name = models.TextField(db_column='Other_Name', blank=True, null=True)  # Field name made lowercase.
    transcript = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    transcript_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wormbase_genetranscript W285'
