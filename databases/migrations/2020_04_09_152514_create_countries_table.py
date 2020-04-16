from orator.migrations import Migration


class CreateCountriesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('countries') as table:
            table.string('name')

            table.integer('case_number')
            table.integer('case_death')
            table.integer('case_recovered')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('countries')
