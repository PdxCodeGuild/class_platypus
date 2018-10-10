from django.core.management.base import BaseCommand





def parse_csv(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')
    headers = lines[0].split(',')
    lines.pop(0)
    data = []
    for line in lines:
        if line == '':
            continue
        row_data = {}
        row_data_text = line.split(',')
        for i in range(len(headers)):
            row_data[headers[i]] = row_data_text[i]
        data.append(row_data)
    return data



from census.models import State, County, CensusDatum


class Command(BaseCommand):

    def handle(self, *args, **options):


        CensusDatum.objects.all().delete()

        data = parse_csv('C:\\Users\\flux\\data\\cc-est2017-alldata-41.csv')
        for datum in data:
            if int(datum['YEAR']) == 10:

                # get or create if it doesn't exist
                state_name = datum['STNAME']
                if State.objects.filter(name=state_name).count() == 0:
                    state = State(name=state_name)
                    state.save()
                else:
                    state = State.objects.get(name=state_name)

                county_name = datum['CTYNAME']
                if County.objects.filter(name=county_name).count() == 0:
                    county = County(name=county_name, state=state)
                    county.save()
                else:
                    county = County.objects.get(name=county_name, state_id=state.id)


                total_population = int(datum['TOT_POP'])
                percent_female = int(datum['TOT_FEMALE'])/total_population

                cd = CensusDatum(county=county, total_population=total_population, percent_female=percent_female)
                cd.save()





