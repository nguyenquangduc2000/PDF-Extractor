import pdftotext
import glob

CONFIG = {
        'Shipper': {
            'row': [2, 8],
            'column': [1, 60],
            'startFlex': False,
            'endObject': 'Consignee',
            'verticalFlex': True
        },
        'Consignee': {
            'row': [9, 17],
            'column': [1, 60],
            'startFlex': True,
            'endObject': 'Notify',
            'verticalFlex': True
        },
        'Notify': {
            'row': [18, 25],
            'column': [1, 60],
            'startFlex': True,
            'endObject': 'M.Vessel/Voyage',
            'verticalFlex': True
        },
        'Reference No.': {
            'row': [1, 2],
            'column': [78, None],
            'startFlex': False,
            'endObject': None,
            'verticalFlex': False
        },
        'Booking No.': {
            'row': [3, 4],
            'column': [78, None],
            'startFlex': False,
            'endObject': None,
            'verticalFlex': False
        },
        'TO': {
            'row': [5, 6],
            'column': [78, None],
            'startFlex': False,
            'endObject': None,
            'verticalFlex': False
        },
        'TEL0': {
            'row': [6, 7],
            'column': [78, None],
            'startFlex': False,
            'endObject': None,
            'verticalFlex': False
        },
        'FAX0': {
            'row': [7, 8],
            'column': [78, None],
            'startFlex': False,
            'endObject': None,
            'verticalFlex': False
        },
        'ATTN0': {
            'row': [8, 9],
            'column': [78, None],
            'startFlex': False,
            'endObject': None,
            'verticalFlex': False
        },
        'FROM': {
            'row': [11, 12],
            'column': [78, None],
            'startFlex': False,
            'endObject': None,
            'verticalFlex': False
        },
        'TEL1': {
            'row': [12, 13],
            'column': [78, None],
            'startFlex': False,
            'endObject': None,
            'verticalFlex': False
        },
        'FAX1': {
            'row': [14, 15],
            'column': [78, None],
            'startFlex': False,
            'endObject': None,
            'verticalFlex': False
        },
        'ATTN1': {
            'row': [15, 16],
            'column': [78, None],
            'startFlex': False,
            'endObject': None,
            'verticalFlex': False
        },
        'E-MAIL': {
            'row': [16, 17],
            'column': [78, None],
            'startFlex': False,
            'endObject': None,
            'verticalFlex': False
        },
        'M.B/L Type': {
            'row': [20, 21],
            'column': [78, None],
            'startFlex': False,
            'endObject': None,
            'verticalFlex': False
        },
        'HS Code': {
            'row': [24, 25],
            'column': [78, None],
            'startFlex': False,
            'endObject': None,
            'verticalFlex': False
        },
        'M.Vessel/Voyage': {
            'row': [25,26],
            'column': [20,58],
            'startFlex': True,
            'endObject': 'Port of Loading',
            'verticalFlex': True
        },
    'Port of Loading': {
        'row': [26, 27],
        'column': [20, 58],
        'startFlex': True,
        'endObject': 'Delivery',
        'verticalFlex': False 
    },
    'Delivery': {
        'row': [27, 28],
        'column': [20, 58],
        'startFlex': True,
        'endObject': 'Mark & Number',
        'verticalFlex': False
    },
    'ETD': {
        'row': [25, 26],
        'column': [66, 85],
        'startFlex': True,
        'endObject': 'Port of Discharge',
        'verticalFlex': False
    },
    'Port of Discharge': {
        'row': [26, 27],
        'column': [80, 94],
        'startFlex': True, 
        'endObject': 'Final Destination', 
        'verticalFlex': False
    },
    'Final Destination': {
        'row': [27, 28],
        'column': [81, 94],
        'startFlex': True,
        'endObject': 'Description of Goods',
        'verticalFlex': False
    },
    'Mark & Number': {
        'row': [31, 36],
        'column': [0, 37],
        'startFlex': True,
        'endObject': 'Freight Prepaid',
        'verticalFlex': True
    },
    'No of Package': {
        'row': [29, 31],
        'column': [32, 44],
        'startFlex': True,
        'endObject': 'Freight Prepaid',
        'verticalFlex': True
    },
    'Description of Goods': {
        'row': [30, 35],
        'column': [44, 80],
        'startFlex': True,
        'endObject': 'Freight Prepaid',
        'verticalFlex': True 
    },
    'Weight': {
        'row': [29, 31], 
        'column': [84, 103],
        'startFlex': True,
        'endObject': 'Freight Prepaid',
        'verticalFlex': True
    },
    'Measurement': {
        'row': [29, 31],
        'column': [102, 115],
        'startFlex': True,
        'endObject': 'Freight Prepaid',
        'verticalFlex': True
    },
    'ETA': {
        'row': [25, 26],
        'column': [95,100],
        'startFlex': True,
        'endObject': 'Port of Discharge',
        'verticalFlex': False
    }
}

CURR_CONFIG = {}
path="VN103933/*.pdf"
files=glob.glob(path)

if __name__ == '__main__':
    for fileName in files:
        print('==============================',fileName,'==============================')
        with open(fileName, "rb") as f:
            pdf = pdftotext.PDF(f)
        page = pdf[0].split("\n")

        # for i in range(len(page)):
        #     print(i)
        #     print([str(k) + page[i][k] for k in range(len(page[i]))])
        data = {}
        for key in CONFIG:
            # print(key)
            row = CONFIG[key]['row']
            column = CONFIG[key]['column']
            # print(row)
            # print(column)
            lines = page[row[0]:row[1]]
            data[key] = '\n'.join([x[column[0]:column[1]] for x in lines])

        for key in data:
            print("%s:\n%s" % (key, data[key]))
        print('==========================================================================')
