analysis = {
  'id': '1234',
  'name': "abc",
  'faults': [
    {
      'id': 'f1',
      'status': 'critical',
      'type': 'lubrication',
     },
         {
      'id': 'f2',
      'status': 'early',
      'type': 'gears',
     },
         {
      'id': 'f3',
      'status': 'critical',
      'type': 'corrosion',
     },
         {
      'id': 'f4',
      'status': 'high',
      'type': 'sensor issue',
     },
    {
      'id': 'f5',
      'status': 'early',
      'type': 'sensor issue',
     },
  ]
}

statuses = [
  {
    'type':'early',
    'count': 0,
  }, 
  {
    'type': 'high',
    'count': 0,
  }, 
  {
    'type': 'critical',
    'count': 0
  },
]