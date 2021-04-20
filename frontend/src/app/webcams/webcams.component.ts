import { Component, OnInit } from '@angular/core';
import { Webcam } from '../webcam';

@Component({
		selector: 'app-webcams',
		templateUrl: './webcams.component.html',
		styleUrls: ['./webcams.component.css']
})
export class WebcamsComponent implements OnInit {
		
		constructor() { }
		
		ngOnInit(): void {
		}

		webcam : Webcam = {
				id: 1,
				country: 'Scotland',
				area: 'Cairngorms',
				name: 'Ptarmigan Building',
				url: 'https://www.cairngormmountain.co.uk/wp-content/uploads/webcams/PtarmiganStation-full.jpg',
				updated: new Date()
		};


}
