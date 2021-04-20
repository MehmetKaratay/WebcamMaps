import { Webcam } from './webcam';

export const WEBCAMS: Webcam[] = [
		{
				id: 1,
				name: 'Ptarmigan Building',
				country: 'Scotland',
				area: 'Cairngorms',
				webpage: 'https://www.cairngormmountain.co.uk/weather-webcams/live-webcams/',
				imgurl: 'https://www.cairngormmountain.co.uk/wp-content/uploads/webcams/PtarmiganStation-full.jpg',
				updated: new Date()
		},
		{
				id: 2,
				name: 'Loch Morlich',
				area: 'Cairngorms',
				country: 'Scotland',
				webpage: 'https://www.cairngormmountain.co.uk/weather-webcams/live-webcams/',
				imgurl: 'https://www.cairngormmountain.co.uk/wp-content/uploads/webcams/morlich-full.jpg',
				updated: new Date()
		},
		{
				id: 3,
				name: 'Aonach Mòr',
				area: 'West Highlands',
				country: 'Scotland',
				webpage: 'https://www.nevisrange.co.uk/webcams/',
				imgurl: 'https://a4.snowcloud.co/webcams/nr/goose.jpeg',
				updated: new Date()
		},
		{
				id: 4,
				name: 'Great Gable',
				area: 'Lake District',
				country: 'England',
				webpage: 'http://www.s213669645.websitehome.co.uk/17.html',
				imgurl: 'https://lvc.wasdale.com/wasdale.jpg',
				updated: new Date()
		}
];
